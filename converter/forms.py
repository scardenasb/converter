from django import forms
from .models import ConverterLength, TYPE_CHOICES, UNIT_CHOICES_LENGTH

class ConverterForm(forms.ModelForm):
    types = forms.CharField(label='', widget=forms.Select(
        choices=TYPE_CHOICES,
        attrs={"class": "form-control form-control-types"}
        ))

    from_unit = forms.FloatField(label='', widget=forms.NumberInput(
        attrs={"class": "form-control from-unit", "placeholder": "Your unit"}
        ))

    unit_types_from = forms.CharField(label='', widget=forms.Select(
        choices=UNIT_CHOICES_LENGTH,
        attrs={"class": "form-control form-control-type-from"}
    ))

    unit_types_to = forms.CharField(label='', widget=forms.Select(
        choices=UNIT_CHOICES_LENGTH,
        attrs={"class": "form-control form-control-type-to"}
    ))

    class Meta:
        model = ConverterLength
        fields = ['from_unit', 'types', 'unit_types_from', 'unit_types_to']


    # def clean_same_types(self, *args, **kwargs):
    #     unit_types_from = self.cleaned_data.get("unit_types_from")
    #     unit_types_to = self.cleaned_data.get("unit_types_to")
    #     if unit_types_from == unit_types_to:
    #         raise forms.ValidationError("Choose a different type unit")
    #     return unit_types_from, unit_types_to
