import unittest
from functions.colour_range import colour_range


class TestColourRange(unittest.TestCase):
    def test_maize_to_white(self):
        result = colour_range(1, 4) # 1=maize, 4=white
        self.assertEqual(result, 4)

    def test_matching_colours(self):
        result = colour_range(55, 55)
        self.assertEqual(result, 1)

    def test_colour_names_fails(self):
        self.assertRaises(TypeError, colour_range, "pear", "mantis")

    def test_loop_around(self):
        result = colour_range(1, 177)
        self.assertEqual(result, 2)

    def test_flip_point(self):
        maize_to_mantis = colour_range(1, 89)
        maize_to_pear = colour_range(1, 90)
        self.assertEqual(maize_to_mantis, maize_to_pear)
