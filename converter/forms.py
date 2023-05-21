from django import forms
from django.utils.translation import gettext as _
from .models import Type, Unit
from djchoices import DjangoChoices, ChoiceItem
from crispy_forms.layout import (
    Layout,
    Div,
    Column,
    Row,
    HTML,
    Submit,
    Fieldset,
)
from crispy_forms.helper import FormHelper


class ConverterForm(forms.Form):
    class Media:
        js = ('/static/js/calc.js',)

        css = {'all': ('css/style.css',)}

    class SystemChoices(DjangoChoices):
        NONE = ChoiceItem(0, ("-------"))
        INTERNACIONAL = ChoiceItem(1, _("SI"))
        AMERICAN = ChoiceItem(2, _("American"))

    unit_type = forms.ModelChoiceField(
        queryset=None,
        empty_label='-------',
        widget=forms.Select(attrs={'class': 'django-select2'}),
    )

    unit_value = forms.FloatField(
        label="",
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your value here: ',
                'maxlength': '12',
                'onkeypress': 'return onlyNumberKey(event)',
            }
        ),
    )

    unit_to = forms.ModelChoiceField(
        label=_("To"),
        required=True,
        queryset=None,
        empty_label='-------',
        widget=forms.Select(
            attrs={
                'class': 'django-select2',
            }
        ),
    )

    unit_from = forms.ModelChoiceField(
        label=_("From"),
        required=True,
        queryset=None,
        empty_label='-------',
        widget=forms.Select(
            attrs={
                'class': 'django-select2',
            }
        ),
    )

    system_from = forms.ChoiceField(
        choices=SystemChoices.choices,
        disabled=True,
        label=_("From"),
        widget=forms.Select(),
    )
    system_to = forms.ChoiceField(
        choices=SystemChoices.choices,
        label=_("To"),
        disabled=True,
        widget=forms.Select(),
    )

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields['unit_type'].queryset = Type.objects.all()
        self.fields['unit_from'].queryset = Unit.objects.none()
        self.fields['unit_to'].queryset = Unit.objects.none()
        self.fields['system_from'].initial = 0
        self.fields['system_to'].initial = 0
        self.fields['unit_value'].initial = ''

        self.helper = FormHelper()
        self.helper.form_class = 'form-parsley'
        self.helper.form_id = 'form-principal'
        self.helper.layout = Layout(
            Div(
                Row(
                    Column(
                        'unit_type',
                    ),
                    css_class='selects',
                ),
                Row(
                    Column('unit_value', css_class="value"),
                    Column(
                        HTML(
                            """
                            <button type="button" id="submit-button" class="button">=</button>
                            """
                        ),
                    ),
                    Column(
                        HTML(
                            """
                            <h2 id='result' class="result"></h2>
                            """
                        ),
                        css_class="result",
                    ),
                    css_class="button-middle",
                ),
                #Row(
                #    Fieldset(
                #        'System',
                #        Column('system_from', css_class="system_from"),
                #        Column('system_to', css_class="system_to"),
                #        css_class='selects border-group-style',
                #    )
                #),
                Row(
                    Fieldset(
                        'Units',
                        Column('unit_from', css_class="from"),
                        Column('unit_to', css_class="to"),
                        css_class='selects border-group-style',
                    ),
                ),
            )
        )
