#!/usr/bin/python3

"""
This module define a class (Square)

Class:
    Square: represents a square

Attributes:
    __size (int): A private instance attribute (the size of a square)
    __position(tuple): Position of square
Method:
    __init__(size): Initializes the size of a square

    area: Calculates the area of a square

    my_print: Prints the value of square to stdout using #

Properties:
    size: This property is use to get the attribute size (getter)
    size: This property with @size.setter set the value of size (setter)

    position: property is use to get the attribute position (getter)
    position: property with @position.setter set the value of position (setter)

"""


class Square:

    """A class that defines a square.

    This class is a representation of a square and provides methods for
    calculating its area and printing it.

    Attributes:
        size (int): The size of the square as a positive integer. Defaults
        to 0.
        position (tuple): The position of the square with respect to stdout.

    Methods:
        area():
            Calculates and returns the area of an instance of the Square.
            Args:
                None.
            Returns:
                int: The area of the square.
        my_print():
            Prints the square with the '#' character
            Args:
                None.
            Returns:
                None.

    Raises:
        TypeError: If 'size' is not an integer or position is not a tuple of
        2 positive integers.
        ValueError: If 'size' is less than 0.
    """

    def __init__(self, size=0, position=(0, 0)):

        """ Initializes a square with size"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ Getter property for size attribute """
        return self.__size

    @property
    def position(self):
        """ Getter property for position attribute """
        return self.__position

    @size.setter
    def size(self, value):
        """ Setter property for size attribute, to set the value """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """ Setter property for position attribute, to set the value """
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        if any(type(i) is not int or i < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):

        """
        Calculates the area of a square

        """

        result = self.size * self.size
        return result

    def my_print(self):

        """
        Prints the value of square to stdout using #

        Prints an empty string if self.size is equal to 0

        """

        square = self.size

        if square == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(square):
                print(' ' * (self.position)[0] + "#" * square)
