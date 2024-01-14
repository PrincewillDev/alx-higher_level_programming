#!/usr/bin/python3

"""
This module define a class (Square)

Class:
    Square: represents a square

Attributes:
    __size: A private instance attribute (the size of a square)

Method:
    __init__(size): Initializes the size of a square

    area: Calculates the area of a square

"""


class Square:

    """
    This class represents a square

    Attributes:
    __size: A private instance attribute (the size of a square)

    Method:
    __init__(size): Initializes the size of a square

    area: Calculates the area of a square


    """

    def __init__(self, size=0):

        """
        Initializes the size of a square

        parameter:
            size: The size of a square

        checks:
            raise TypeError if size is not an integer

            raise ValueError if size is less than 0

        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):

        """
        Calculates the area of a square

        """
        result = self.__size * self.__size
        return result
