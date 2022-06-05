from django.shortcuts import render

from .models import Unit, UnitTo
from .forms import ConverterForm

# Create your views here.
def index(request):
    template = 'converter/index.html'
    context = {}
    context['form'] = ConverterForm()
    used_form = ConverterForm()

    if request.method == 'GET':
        return render(request, template, context)

# TODO: look for a way to let previous form data selected
    if request.method == 'POST':
        used_form = ConverterForm(request.POST)

        if used_form.is_valid():
            unit_converted = used_form.save()
            from_unit = unit_converted.from_unit
            to_unit = unit_converted.to_unit
            context['from_unit'] = from_unit
            context['to_unit'] = to_unit
            return render(request, template, context)

    context['errors'] = used_form.errors

    return render(request, template, context)

# AJAX
def load_units(request):
    context = {}
    type_id = request.GET.get('type_id')
    units = Unit.objects.filter(type_id=type_id).all()
    units_to = UnitTo.objects.filter(type_id=type_id).all()
    context['units'] = units
    context['units_to'] = units_to
    return render(request, 'converter/units_dropbox_control.html', context)
