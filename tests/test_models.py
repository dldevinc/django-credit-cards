import datetime
from django.core.exceptions import ValidationError
from django.test import TestCase
from .app.models import CardNumber, CardExpiry, CardCode


class CardNumberTest(TestCase):
    def test_input(self):
        obj = CardNumber(number='30569309025904')
        obj.clean_fields()
        self.assertEqual(obj.number, '30569309025904')

    def test_input_with_spaces(self):
        obj = CardNumber(number='4111 1111 1111 1111')
        obj.clean_fields()
        self.assertEqual(obj.number, '4111111111111111')

    def test_input_with_dashes(self):
        obj = CardNumber(number='3782-8224631-0005')
        obj.clean_fields()
        self.assertEqual(obj.number, '378282246310005')

    def test_input_invalid_luhn(self):
        obj = CardNumber(number='4111 1111 1111 1112')
        self.assertRaises(ValidationError, obj.clean_fields)


class CardExpiryTest(TestCase):
    def test_input_invalid_string(self):
        obj = CardExpiry(expiry='something')
        self.assertRaises(ValidationError, obj.clean_fields)

    def test_input_short_string(self):
        obj = CardExpiry(expiry='7/30')
        obj.clean_fields()
        self.assertEqual(obj.expiry, datetime.date(2030, 7, 31))

    def test_input_invalid_short_string(self):
        obj = CardExpiry(expiry='13/18')
        self.assertRaises(ValidationError, obj.clean_fields)

    def test_input_long_string(self):
        obj = CardExpiry(expiry='01/2030')
        obj.clean_fields()
        self.assertEqual(obj.expiry, datetime.date(2030, 1, 31))

    def test_input_invalid_long_string(self):
        obj = CardExpiry(expiry='01/200')
        self.assertRaises(ValidationError, obj.clean_fields)

    def test_input_date(self):
        obj = CardExpiry(expiry=datetime.date(2030, 11, 5))
        obj.clean_fields()
        self.assertEqual(obj.expiry, datetime.date(2030, 11, 30))

    def test_input_passed_date(self):
        obj = CardExpiry(expiry=datetime.date(2000, 7, 12))
        obj.clean_fields()
        self.assertEqual(obj.expiry, datetime.date(2000, 7, 31))

    def test_input_datetime(self):
        obj = CardExpiry(expiry=datetime.datetime(2030, 12, 15, 23, 59, 59))
        obj.clean_fields()
        self.assertEqual(obj.expiry, datetime.date(2030, 12, 31))


class CardCodeTest(TestCase):
    def test_input_three_digits(self):
        obj = CardCode(code='111')
        obj.clean_fields()
        self.assertEqual(obj.code, '111')

    def test_input_four_digits(self):
        obj = CardCode(code='1111')
        obj.clean_fields()
        self.assertEqual(obj.code, '1111')

    def test_input_invalid(self):
        obj = CardCode(code='abc')
        self.assertRaises(ValidationError, obj.clean_fields)

    def test_input_less_than_minimum_lenght(self):
        obj = CardCode(code='66')
        self.assertRaises(ValidationError, obj.clean_fields)

    def test_input_more_than_maximum_lenght(self):
        obj = CardCode(code='66666')
        self.assertRaises(ValidationError, obj.clean_fields)
