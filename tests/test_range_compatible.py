import unittest
from functions.range_compatible import range_compatible


class TestRangeCompatible(unittest.TestCase):
    def test_zero_with_max_positive(self):
        result = range_compatible(0, 88)
        self.assertEqual(result, True)

    def test_zero_with_max_negative(self):
        result = range_compatible(0, -88)
        self.assertEqual(result, True)

    def test_small_range_around_goal(self):
        result = range_compatible(-2, 4)
        self.assertEqual(result, True)

    def test_small_range_above_goal(self):
        result = range_compatible(4, 5)
        self.assertEqual(result, False)

    def test_small_range_below_goal(self):
        result = range_compatible(-2, -4)
        self.assertEqual(result, False)

    def test_maximum_possible_range(self):
        result = range_compatible(-1, 87)  # equivalent to maize and mantis wrt cream
        self.assertEqual(result, True)

    def test_flips_other_way(self):
        result = range_compatible(-1, 88)  # equivalent to maize and pear wrt cream
        self.assertEqual(result, False)
