from django.shortcuts import render
from .forms import ConverterForm
from .models import ConverterLength

# Create your views here.

def index(request):
    template = 'converter/index.html'
    context = {}
    context['form'] = ConverterForm()
    used_form = ConverterForm()

    if request.method == 'GET':
        return render(request, template, context)

    elif request.method == 'POST':
        used_form = ConverterForm(request.POST or None)

        if used_form.is_valid():
            unit_converted = used_form.save()
            from_unit = unit_converted.from_unit
            # used_form = ConverterForm()
            to_unit = unit_converted.to_unit
            context['to_unit'] = to_unit
            context['from_unit'] = from_unit
            return render(request, template, context)

        context['errors'] = used_form.errors

        return render(request, template, context)




