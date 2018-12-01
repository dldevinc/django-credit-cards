from django.db import models
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField


class CardNumber(models.Model):
    number = CardNumberField('card number')


class CardExpiry(models.Model):
    expiry = CardExpiryField('expiry date', null=True)


class CardCode(models.Model):
    code = SecurityCodeField('security code')
