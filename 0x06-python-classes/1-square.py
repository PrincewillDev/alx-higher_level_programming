#!/usr/bin/python3

"""
This module defines a class (Square)

Class:
    Square: Represent a square

Attribute:
   __size: A private instance attribute (The size of square).

Method:
    __init__: Initializes a square with a given size.

"""


class Square:

    """
    Represents a square with a private instance attribute of __size.

    Attributes:
        __size (int): The size of square (a private instance attribute)

    Method:
        __init__(size): Initializes the size of square

    """

    def __init__(self, size):

        """
        Initializes the size of the square

        parameters:
            size (int): The size of the square.

        """
        self.__size = size
