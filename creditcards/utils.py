import re
import calendar
import datetime

LUHN_ODD_LOOKUP = (0, 2, 4, 6, 8, 1, 3, 5, 7, 9)    # sum_of_digits(index * 2)
re_non_digits = re.compile(r'[^\d]+')


def get_digits(value):
    """
    Get all digits from input string.

    :type value: str
    :rtype: str
    """
    if not value:
        return ''
    return re_non_digits.sub('', str(value))


def luhn(number):
    """
    Validate credit card number with Luhn's Algorithm.

    Source:
    https://github.com/django/django-localflavor/blob/master/localflavor/generic/checksums.py

    :type number: str
    :rtype: bool
    """
    number = str(number)
    try:
        evens = sum(int(c) for c in number[-1::-2])
        odds = sum(LUHN_ODD_LOOKUP[int(c)] for c in number[-2::-2])
        return (evens + odds) % 10 == 0
    except ValueError:
        return False


def expiry_date(year, month):
    """
    Return the last day of month.

    :type year: int
    :type month: int
    :rtype: datetime.date
    """
    weekday, day_count = calendar.monthrange(year, month)
    return datetime.date(year, month, day_count)
