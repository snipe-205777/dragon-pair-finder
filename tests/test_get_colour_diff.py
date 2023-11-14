import unittest
from functions.get_colour_diff import get_colour_diff


class TestGetColourDiff(unittest.TestCase):
    def test_equal_colours(self):
        result = get_colour_diff(5, 5)
        self.assertEqual(result, 0)

    def test_positive_is_down_from_goal(self):
        result = get_colour_diff(10, 5)
        self.assertEqual(result, 5)

    def test_negative_is_up_from_goal(self):
        result = get_colour_diff(4, 1)
        self.assertEqual(result, 3)

    def test_positive_when_wrapping_round(self):
        result = get_colour_diff(2, 176)
        self.assertEqual(result, 3)

    def test_negative_when_wrapping_round(self):
        result = get_colour_diff(177, 1)
        self.assertEqual(result, -1)

    def test_mantis_to_maize(self):
        result = get_colour_diff(89, 1)
        self.assertEqual(result, 88)
    
    def test_pear_to_maize(self):
        result = get_colour_diff(90, 1)
        self.assertEqual(result, -88)
