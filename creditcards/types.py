import re
from .utils import get_digits

CC_TYPE_GENERIC = 0
CC_TYPE_VISA = 1
CC_TYPE_AMEX = 2
CC_TYPE_DINERS = 3
CC_TYPE_DISCOVER = 4
CC_TYPE_MASTERCARD = 5
CC_TYPE_ELO = 6
CC_TYPE_JCB = 7
CC_TYPE_MIR = 8
CC_TYPE_UNIONPAY = 9

# Based on Chromium source code:
# https://github.com/chromium/chromium/blob/master/components/autofill/core/browser/data_model/credit_card.cc
#
# Note that UnionPay validated by Luhn checksum:
# https://github.com/chromium/chromium/commit/c2e6e3149e3abd4de5b9969c2ece3caa019c3540
CC_TYPES = (
    (CC_TYPE_ELO, {
        'title': 'Elo',
        'regex': re.compile(r'^(?:431274|451416|5067|5090|627780|636297)')
    }),
    (CC_TYPE_VISA, {
        'title': 'Visa',
        'regex': re.compile(r'^4')
    }),
    (CC_TYPE_AMEX, {
        'title': 'American Express',
        'regex': re.compile(r'^3[47]')
    }),
    (CC_TYPE_DINERS, {
        'title': 'Diners Club',
        'regex': re.compile(r'^3(?:0[0-5]|095|[689])')
    }),
    (CC_TYPE_DISCOVER, {
        'title': 'Discover Card',
        'regex': re.compile(r'^6(?:011|4[4-9]|5)')
    }),
    (CC_TYPE_JCB, {
        'title': 'JCB',
        'regex': re.compile(r'^35(?:2[89]|[3-8])')
    }),
    (CC_TYPE_MIR, {
        'title': 'MIR',
        'regex': re.compile(r'^220[0-4]')
    }),
    (CC_TYPE_UNIONPAY, {
        'title': 'UnionPay',
        'regex': re.compile(r'^62')
    }),
    (CC_TYPE_MASTERCARD, {
        'title': 'MasterCard',
        'regex': re.compile(r'^(?:5[1-5]|222[1-9]|22[3-9]|2[3-6]|27[01]|2720)')
    }),
)

CC_TYPE_CHOICES = (
    (CC_TYPE_AMEX, 'American Express'),
    (CC_TYPE_DINERS, 'Diners Club'),
    (CC_TYPE_DISCOVER, 'Discover Card'),
    (CC_TYPE_ELO, 'Elo'),
    (CC_TYPE_JCB, 'JCB'),
    (CC_TYPE_MASTERCARD, 'MasterCard'),
    (CC_TYPE_MIR, 'MIR'),
    (CC_TYPE_UNIONPAY, 'UnionPay'),
    (CC_TYPE_GENERIC, 'Generic'),
)


def get_type(number):
    """
    Gets credit card type given number.

    :type number: str
    :rtype: int
    """
    number = get_digits(number)
    for code, record in CC_TYPES:
        if re.match(record['regex'], number):
            return code
    return CC_TYPE_GENERIC
