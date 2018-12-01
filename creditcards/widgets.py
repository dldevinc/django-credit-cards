from django.forms import widgets


class TelephoneInput(widgets.TextInput):
    input_type = 'tel'


class ExpiryDateWidget(widgets.TextInput):
    pass
