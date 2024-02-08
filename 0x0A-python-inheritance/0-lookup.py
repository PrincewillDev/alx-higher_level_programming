#!/usr/bin/python3

"""
This module checks and returns attributes
and methods of an object

"""


def lookup(obj):
    """
    This function takes an object and returns the
    attribute and method of the object

    Parameters:
    obj: This is the object to be checked and returns
    its available attributes and methods.

    Returns:
    Attributes and Methods of obj

    """
    return dir(obj)
