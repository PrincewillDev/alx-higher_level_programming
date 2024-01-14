#!/usr/bin/python3
"""
This module defines a class (Square)

Class:
    Square: Represents a square.

Attribute:
    __size: A private instance attribute (the size of a square)

Method:
    __init__(size): Initializes the size of the square.

"""


class Square:

    """
    Represents a square

    Attribute:
    __size: A private instance attribute (the size of a square)

    Method:
    __init__(size): Initializes the size of the square.

    """
    def __init__(self, size=0):
        """
        Initializes the size of square

        parameter:
            size(int): Represents the size of a square

        checks:
            raise TypeError: if size is not an integer
            raise ValueError: if size is less than 0

        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
