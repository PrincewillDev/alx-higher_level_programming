"""
This modules tests the Base class using unittest

Class:
    TestBaseclass: This class inherits TestCase class
    from unittest modules and test Base class.
"""
import unittest
import os
from models.base import Base


class TestBaseclass(unittest.TestCase):
    """
    This Class test the Base class while inheriting
    TestCase class from unittest module.

    Methods:
        test_file: checks if the module Base exists

        test_nb_object_and_id_as_none: checks if

        __nb_objects works as expected and if the Base class
        behaves as expected when id is None.

        test_init_with_id: Testing the init constructor
        by passing the instance attribute a value

    """
    def test_file(self):
        self.assertTrue(os.path.isfile('./models/base.py'))

    def test_nb_object_and_id_as_none(self):
        self.assertEqual(Base.get_nb_objects(), 0)

        obj1_without_id = Base()
        obj2_without_id = Base()
        obj3_without_id = Base()

        self.assertEqual(obj1_without_id.id, 1)
        self.assertEqual(obj2_without_id.id, 2)
        self.assertEqual(obj3_without_id.id, 3)

        self.assertEqual(Base.get_nb_objects(), 3)

    def test_init_with_id(self):
        object_with_id = Base(90)
        self.assertEqual(object_with_id.id, 90)


if __name__ == "__main__":
    unittest.main()
