import datetime
from django.test import TestCase
from .app.forms import CardNumber, CardExpiry, CardCode


class CardNumberTest(TestCase):
    def test_input_plain(self):
        form = CardNumber({
            'number': '30569309025904'
        })
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['number'], '30569309025904')

    def test_input_with_spaces(self):
        form = CardNumber({
            'number': '4111 1111 1111 1111'
        })
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['number'], '4111111111111111')

    def test_input_with_dashes(self):
        form = CardNumber({
            'number': '3782-8224631-0005'
        })
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['number'], '378282246310005')

    def test_long_input_with_dashes(self):
        form = CardNumber({
            'number': '4532-2616-1547-6013542'
        })
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['number'], '4532261615476013542')

    def test_too_short(self):
        form = CardNumber({
            'number': '4111 1111 112'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['number'].data[0].code, 'min_length')

    def test_too_long(self):
        form = CardNumber({
            'number': '4111 1111 1111 1111 1115'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['number'].data[0].code, 'max_length')

    def test_invalid_luhn(self):
        form = CardNumber({
            'number': '4111-1111-1111-1110'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['number'].data[0].code, 'invalid')


class CardExpiryTest(TestCase):
    def test_invalid_string(self):
        form = CardExpiry({
            'expiry': '2018-11-10'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['expiry'].data[0].code, 'invalid')

    def test_short_string(self):
        form = CardExpiry({
            'expiry': '7/30'
        })
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['expiry'], datetime.date(2030, 7, 31))

    def test_invalid_short_string(self):
        form = CardExpiry({
            'expiry': '13/18'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['expiry'].data[0].code, 'invalid')

    def test_long_string(self):
        form = CardExpiry({
            'expiry': '01/2022'
        })
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['expiry'], datetime.date(2022, 1, 31))

    def test_invalid_long_string(self):
        form = CardExpiry({
            'expiry': '01/200'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['expiry'].data[0].code, 'invalid')

    def test_date_object(self):
        form = CardExpiry({
            'expiry': datetime.date(2030, 11, 5)
        })
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['expiry'], datetime.date(2030, 11, 30))

    def test_passed_date(self):
        form = CardExpiry({
            'expiry': '10/09'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['expiry'].data[0].code, 'date_passed')

        form = CardExpiry({
            'expiry': '06/1988'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['expiry'].data[0].code, 'date_passed')

        form = CardExpiry({
            'expiry': datetime.date(2012, 11, 8)
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['expiry'].data[0].code, 'date_passed')

    def test_input_datetime(self):
        form = CardExpiry({
            'expiry': datetime.datetime(2030, 12, 15, 23, 59, 59)
        })
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['expiry'], datetime.date(2030, 12, 31))


class CardCodeTest(TestCase):
    def test_input_three_digits(self):
        form = CardCode({
            'code': '111'
        })
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['code'], '111')

    def test_input_four_digits(self):
        form = CardCode({
            'code': '1111'
        })
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['code'], '1111')

    def test_input_invalid(self):
        form = CardCode({
            'code': 'abc'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['code'].data[0].code, 'invalid')

    def test_input_less_than_minimum_lenght(self):
        form = CardCode({
            'code': '66'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['code'].data[0].code, 'invalid')

    def test_input_more_than_maximum_lenght(self):
        form = CardCode({
            'code': '66666'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['code'].data[0].code, 'invalid')
