import unittest
from functions.test_for_relation import test_for_relation


class TestTestForRelation(unittest.TestCase):
    def test_related_dragons(self):
        result = test_for_relation("ABCD", "DEFG")
        self.assertEqual(result, True)

    def test_unrelated_dragons(self):
        result = test_for_relation("ABC", "DEF")
        self.assertEqual(result, False)

    def test_upper_and_lower_are_not_related(self):
        result = test_for_relation("ABC", "abc")
        self.assertEqual(result, False)
