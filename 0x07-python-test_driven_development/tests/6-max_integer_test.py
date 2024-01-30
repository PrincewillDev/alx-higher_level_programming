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
	
