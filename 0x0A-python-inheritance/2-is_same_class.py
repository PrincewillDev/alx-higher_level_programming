#!/usr/bin/python3

"""
This module checks if an object
is a exactly an instance of a specified
class and return True or False

"""


def is_same_class(obj, a_class):
    """
    This function checks if the obj is an instane
    of a specified class

    Parameters:
    obj: This is the object
    a_class : This is the specified class

    Returns:
    True: if obj is an instance of a class
    False: if obj is not an instance of a class

    """
    return isinstance(obj, a_class)
