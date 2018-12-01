import re
import calendar
import datetime

LUHN_ODD_LOOKUP = (0, 2, 4, 6, 8, 1, 3, 5, 7, 9)    # sum_of_digits(index * 2)
re_non_digits = re.compile(r'[^\d]+')


def get_digits(value):
    if not value:
        return ''
    return re_non_digits.sub('', str(value))


def luhn(candidate):
    """
    Source:
    https://github.com/django/django-localflavor/blob/master/localflavor/generic/checksums.py
    """
    if not isinstance(candidate, str):
        candidate = str(candidate)
    try:
        evens = sum(int(c) for c in candidate[-1::-2])
        odds = sum(LUHN_ODD_LOOKUP[int(c)] for c in candidate[-2::-2])
        return (evens + odds) % 10 == 0
    except ValueError:
        return False


def exiry_date(year, month):
    weekday, day_count = calendar.monthrange(year, month)
    return datetime.date(year, month, day_count)
