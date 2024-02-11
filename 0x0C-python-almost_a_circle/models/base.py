#!/usr/bin/python3

"""
This module contains 'Base Class'

Class:
    Base: This class is the parent class of all class to be created
"""


class Base:
    """
    This class is the Base Class

    Attribute:
        __nb_objects: This is a class attribute that keep track
        of the number of instance created by incrementing __nb_objects

        id: This is an instance attribute

    Method:
        __init__: The constructor

        get_nb_objects: This is a class method that return the
        class private attribute < __nb_objects >
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def get_nb_objects(cls):
        return cls.__nb_objects
