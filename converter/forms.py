from django import forms
from .models import Unit, ConverterLength, UnitTo

class ConverterForm(forms.ModelForm):
    class Meta:
        model = ConverterLength
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['unit'].queryset = Unit.objects.none()
        self.fields['unit_to'].queryset = UnitTo.objects.none()
        self.fields['from_unit'].widget.attrs.update({'placeholder':'your unit here','required':True})

        if 'type' in self.data:
            try:
                type_id = int(self.data.get('type'))
                self.fields['unit'].queryset = Unit.objects.filter(type_id=type_id).order_by('name')
                self.fields['unit_to'].queryset = UnitTo.objects.filter(type_id=type_id).order_by('name')
            except (ValueError, TypeError):
                pass  
        elif self.instance.pk:
            self.fields['unit'].queryset = self.instance.type.unit_set.order_by('name')
            self.fields['unit_to'].queryset = self.instance.type.unit_to_set.order_by('name')
