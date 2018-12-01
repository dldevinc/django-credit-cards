from django.test import TestCase
from creditcards.utils import luhn


class UtilsTest(TestCase):
    def test_luhn(self):
        valid = [
            '000000018',
            '0000000000000000',
            '30569309025904',
            '3566002020360505',
            '378282246310005',
            '4111111111111111',
            '4242424242424242',
            '5105105105105100',
            '5555555555554444',
            '6011111111111117',
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
