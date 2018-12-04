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
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField

class Payment(models.Model):
    cc_number = CardNumberField(_('card number'))
    cc_expiry = CardExpiryField(_('expiration date'))
    cc_code = SecurityCodeField(_('security code'))
```

Or to your forms:
```python
from creditcards.forms import CardNumberField, CardExpiryField, SecurityCodeField

class PaymentForm(forms.Form):
    cc_number = CardNumberField(label='Card Number')
    cc_expiry = CardExpiryField(label='Expiration Date')
    cc_code = SecurityCodeField(label='CVV/CVC')
```

### Credit Card Type Detection
```python
from creditcards import types

assert types.get_type('4444333322221111') == types.CC_TYPE_VISA
assert types.get_type('343434343434343') == types.CC_TYPE_AMEX
assert types.get_type('0000000000000000') == types.CC_TYPE_GENERIC
```

## License
Copyright (c) 2018 Mihail Mishakin Released under the MIT license (see LICENSE)
