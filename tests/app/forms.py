from django import forms
from creditcards.forms import CardNumberField, CardExpiryField, SecurityCodeField


class CardNumber(forms.Form):
    number = CardNumberField()


class CardExpiry(forms.Form):
    expiry = CardExpiryField()


class CardCode(forms.Form):
    code = SecurityCodeField()

