#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestforMaxInt(unittest.TestCase):
    def test_for_if_list_is_empty(self):
        result = max_integer(list=[])
        self.assertIsNone(result)

    def test_normal_case(self):
        """Test with normal cases"""
        self.assertEqual(max_integer([1, 5, 2, 4]), 5)
        self.assertEqual(max_integer([-2, 7, 0, -10]), 7)
        self.assertEqual(max_integer([-5, -0.5, -25, -15]), -0.5)
        self.assertEqual(max_integer([0, -2, -10]), 0)
        self.assertEqual(max_integer([-7]), -7)
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([15, 3, 2, 4]), 5)



    def test_for_negative_numbers(self):
        self.assertRaises(TypeError, max_integer, 2)
        self.assertRaises(TypeError, max_integer, None)
        self.assertRaises(TypeError, max_integer, [1, -5, 'a', 7])
        self.assertRaises(TypeError, max_integer, [1, -5, [6], 7])

    def test_for_one_item_in_list(self):
        result = max_integer(list=[3])
        self.assertEqual(result, 3)

if __name__ == "__main__":
    unittest.main()
