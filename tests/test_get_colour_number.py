import unittest
from colours import colours
from functions.get_colour_number import get_colour_number


class TestGetColourNumber(unittest.TestCase):
    def test_maize(self):
        result = get_colour_number("maize")
        self.assertEqual(result, 1)

    def test_input_is_not_case_sensitive(self):
        result = get_colour_number("SPEARMINT")
        self.assertEqual(result, 75)
