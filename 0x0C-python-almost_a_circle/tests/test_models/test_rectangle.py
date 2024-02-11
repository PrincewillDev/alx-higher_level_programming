"""
This module tests the Rectangle Class using Unittest

Class:
    TestRectangleClass: This class inherits TestCase class
    from unittest module and test the Rectangle class.
"""
import unittest
import os
from models.rectangle import Rectangle

class TestRectangleClass(unittest.TestCase):
    """
    This Class test the Rectangle class while inheriting
    TestCase class from unittest module.

    Method:
        test_if_module_is_present: This test checks if the module
        <rectangle> exists.

    """
    def test_if_module_is_present(self):
        self.assertTrue(os.path.isfile('./models/base.py'))

    def test_rectangle_instance_attribute(self):
        rec_object_1 = Rectangle(12, 3, 0, 0)
        rec_object_2 = Rectangle(14, 4, 2, 9, 34)

        self.assertEqual(rec_object_1.width, 12)
        self.assertEqual(rec_object_1.height, 3)
        self.assertEqual(rec_object_1.x, 0)
        self.assertEqual(rec_object_1.y, 0)
        self.assertEqual(rec_object_1.id, 1)

        self.assertEqual(rec_object_2.x, 2)
        self.assertEqual(rec_object_2.y, 9)
        self.assertEqual(rec_object_2.id, 34)
