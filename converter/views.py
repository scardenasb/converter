from django.views.generic import View, FormView
from django.http import JsonResponse

from .models import Unit, Type
from .forms import ConverterForm
from .tools import unit_calculator


class Converter(FormView):

    template_name = 'converter/converter.html'
    form_class = ConverterForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()

        return kwargs

    def form_invalid(self, form):
        return super().form_invalid(form)

    def form_valid(self, form):

        if form.errors:
            form.add_error('', 'ERROR')
            return self.form_invalid(form)

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['form'] = self.form_class()

        return context


class AjaxUnit(View):
    def get(self, request):
        type_id = request.GET.get('type_id')

        data = []
        units_qs = Unit.objects.filter(unit_type_id=type_id).values(
            'id', 'abbreviation'
        )

        for i in units_qs:
            qs = {
                'id': i['id'],
                'abbreviation': i['abbreviation'],
            }
            data.append(qs)

        response = {'status': 200, 'data': data}
        return JsonResponse(response)


class AjaxResult(View):
    def get(self, request):
        type_id = request.GET.get('type_id')
        from_id = request.GET.get('from_id')
        to_id = request.GET.get('to_id')
        value = request.GET.get('value')
        value = float(value.replace(',', '.'))

        type_unit = Type.objects.filter(id=type_id).values('code').first()
        from_exp = (
            Unit.objects.filter(id=from_id).values('unit_exponent').first()
        )
        to_exp = (
            Unit.objects.filter(id=to_id)
            .values('unit_exponent', 'abbreviation')
            .first()
        )

        #if type_unit['code'] == 1:
        result = unit_calculator(
            float(value),
            from_exp['unit_exponent'],
            to_exp['unit_exponent'],
        )
        text = f"{result:,} {to_exp['abbreviation']}'s"

        data = {}
        data['text'] = text

        response = {'status': 200, 'data': data}
        return JsonResponse(response)
