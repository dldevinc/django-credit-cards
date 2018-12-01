# django-credit-cards
A Django app providing database and form fields for credit cards.

## Compatibility
* `django` >= 1.8
* `python` >= 3

## Quickstart
Install django-credit-cards:
```bash
pip install django-credit-cards
```

Then add it to your models:
```python
from creditcard.models import CardNumberField, CardExpiryField, SecurityCodeField

class Payment(models.Model):
    cc_number = CardNumberField(_('card number'))
    cc_expiry = CardExpiryField(_('expiration date'))
    cc_code = SecurityCodeField(_('security code'))
```

Or to your forms:
```python
from creditcard.forms import CardNumberField, CardExpiryField, SecurityCodeField

class PaymentForm(forms.Form):
    cc_number = CardNumberField(label='Card Number')
    cc_expiry = CardExpiryField(label='Expiration Date')
    cc_code = SecurityCodeField(label='CVV/CVC')
```
