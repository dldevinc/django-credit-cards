import datetime
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _
from . import utils


@deconstructible
class CCNumberValidator:
    message = _('Enter a valid credit card number.')
    code = 'invalid'

    def __init__(self, message=None, code=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):
        if not utils.luhn(utils.get_digits(value)):
            raise ValidationError(self.message, code=self.code)

    def __eq__(self, other):
        return (
                isinstance(other, self.__class__) and
                (self.message == other.message) and
                (self.code == other.code)
        )


@deconstructible
class CSCValidator(RegexValidator):
    regex = r'^\d{3,4}$'
    message = _('Enter a valid security code.')
    code = 'invalid'


@deconstructible
class ExpiryDateValidator:
    message = _('This date has passed.')
    code = 'date_passed'

    def __init__(self, message=None, code=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):
        expiry_date = utils.expiry_date(value.year, value.month)
        if expiry_date < datetime.date.today():
            raise ValidationError(self.message, code=self.code)

    def __eq__(self, other):
        return (
                isinstance(other, self.__class__)
                and (self.message == other.message)
                and (self.code == other.code)
        )
