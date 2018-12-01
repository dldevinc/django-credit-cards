import datetime
from django import forms
from .validators import LuhnValidator, CSCValidator, ExpiryDateValidator
from .widgets import TelephoneInput, ExpiryDateWidget
from . import utils

__all__ = ['CardNumberField', 'CardExpiryField', 'SecurityCodeField']


class CardNumberField(forms.CharField):
    widget = TelephoneInput
    default_validators = [LuhnValidator()]

    def to_python(self, value):
        return utils.get_digits(super().to_python(value))

    def widget_attrs(self, widget):
        attrs = super().widget_attrs(widget)
        attrs.update({
            'pattern': '[-\d\s]*',
            'x-autocompletetype': 'cc-number',
            'autocompletetype': 'cc-number',
            'autocorrect': 'off',
            'spellcheck': 'off',
            'autocapitalize': 'off',
        })
        return attrs


class CardExpiryField(forms.DateField):
    widget = ExpiryDateWidget
    input_formats = ['%m/%y', '%m/%Y']
    default_validators = [ExpiryDateValidator()]

    def prepare_value(self, value):
        if isinstance(value, (datetime.date, datetime.datetime)):
            return value.strftime('%m/%y')
        return value

    def to_python(self, value):
        value = super().to_python(value)
        if isinstance(value, datetime.date):
            value = utils.exiry_date(value.year, value.month)
        return value

    def widget_attrs(self, widget):
        attrs = super().widget_attrs(widget)
        attrs.update({
            'pattern': '\d+/\d+',
            'placeholder': 'MM/YY',
            'x-autocompletetype': 'cc-exp',
            'autocompletetype': 'cc-exp',
            'autocorrect': 'off',
            'spellcheck': 'off',
            'autocapitalize': 'off',
        })
        return attrs


class SecurityCodeField(forms.CharField):
    widget = TelephoneInput
    default_validators = [CSCValidator()]

    def widget_attrs(self, widget):
        attrs = super().widget_attrs(widget)
        attrs.update({
            'pattern': '\d*',
            'x-autocompletetype': 'cc-csc',
            'autocompletetype': 'cc-csc',
            'autocorrect': 'off',
            'spellcheck': 'off',
            'autocapitalize': 'off',
        })
        return attrs
