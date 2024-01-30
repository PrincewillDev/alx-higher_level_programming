#!/usr/bin/python3

"""
This module defines a function to print the
first and last name of a user

Attributes:
    None

Function:
    say_my_name: Print first and last name of a user

"""


def say_my_name(first_name, last_name=""):
    """ This Function print first and last name
        of a user

        Args:
            first_name: Firstname of the user
            last_name: Lastname of the user

        Return:
            None

        Raises:
            TypeError: if first and lastname are not strings
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
