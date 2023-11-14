import unittest
from functions.number_direction import number_direction


class TestNumberDirection(unittest.TestCase):
    def test_zero_is_zero(self):
        result = number_direction(0)
        self.assertEqual(result, 0)

    def test_positive_is_one(self):
        result = number_direction(1)
        self.assertEqual(result, 1)

    def test_negative_is_minus_one(self):
        result = number_direction(-1)
        self.assertEqual(result, -1)

    def test_any_size_positive_is_one(self):
        result = number_direction(785743847921)
        self.assertEqual(result, 1)

    def test_any_size_negative_is_minus_one(self):
        result = number_direction(-43143285729)
        self.assertEqual(result, -1)
