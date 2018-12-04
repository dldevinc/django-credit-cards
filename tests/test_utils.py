from datetime import date
from django.test import TestCase
from creditcards.utils import luhn, expiry_date


class UtilsTest(TestCase):
    def test_luhn(self):
        valid = [
            '000000018',
            '0000000000000000',
            '2204883716636153',
            '2200111234567898',
            '2200481349288130',
            '30569309025904',
            '3566002020360505',
            '378282246310005',
            '371449635398431',
            '378734493671000',
            '38520000023237',
            '4012888888881881',
            '4111111111111111',
            '4242424242424242',
            '4532261615476013542',
            '5105105105105100',
            '5555555555554444',
            '5610591081018250',
            '6011111111111117',
            '6331101999990016',
        ]
        invalid = [
            '4242424242424240',
            '4242424242424241',
            '4242424242424243',
            '4242424242424244',
            '4242424242424245',
            '4242424242424246',
            '4242424242424247',
            '4242424242424248',
            '4242424242424249',
        ]

        for number in valid:
            with self.subTest(number):
                self.assertTrue(luhn(number))
        for number in invalid:
            with self.subTest(number):
                self.assertFalse(luhn(number))

    def test_expiry_date(self):
        tests = {
            (2015, 6): date(2015, 6, 30),
            (2016, 2): date(2016, 2, 29),
            (2018, 2): date(2018, 2, 28),
            (2018, 12): date(2018, 12, 31),
            (2022, 9): date(2022, 9, 30),
        }
        for (year, month), days in tests.items():
            with self.subTest('{}-{}'.format(year, month)):
                self.assertEqual(expiry_date(year, month), days)
