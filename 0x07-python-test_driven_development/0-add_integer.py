#!/usr/bin/python3

"""
Adds two integers
Parameters: a, b
Returns: int: The sum of a and b
"""


def add_integer(a, b=98):
    """ Adds two intgers
        Returns: int: The sum of a and b
    """
    if not isinstance(a, (int, float)):
        """ raise TypeError if a is not an integer """
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        """ raise TypeError if b is not an integer """
        raise TypeError("b must be an integer")

    result = int(a + b)
    return result
