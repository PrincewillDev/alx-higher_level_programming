#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestforMaxInt(unittest.TestCase):
    def test_for_if_list_is_empty(self):
        result = max_integer(list=[])
        self.assertIsNone(result)

    def test_for_correct_output(self):
        result = max_integer(list=[1,2,3,4])
        self.assertEqual(result, 4)
	
    def test_for_max_at_the_beginning(self):
        result = max_integer(list=[10,2,3,4])
        self.assertEqual(result, 10)
	
    def test_for_max_in_the_middle(self):
        result = max_integer(list=[1,2,3,8,4,5,6])
        self.assertEqual(result, 8)

    def test_for_negative_numbers(self):
        test_list = [1,2,3,0,3]
        for number in test_list:
           self.assertGreaterEqual(number, 0)

    def test_for_one_item_in_list(self):
        result = max_integer(list=[3])
        self.assertEqual(result, 3)
