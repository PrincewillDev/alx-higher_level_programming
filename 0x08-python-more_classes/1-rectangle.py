#!/usr/bin/python3

"""
This module creates an class that defines
a rectangle width and height

Class:
    Rectangle: Defines a rectangle

Attribute:
    width: The width of a rectangle
    Height: The height of a rectangle

Method:
    __init__(width, height): width and height of a rectangle

"""


class Rectangle:
    """
    This class defines a rectangle by its width and heights

    Attribute:
    width: The width of a rectangle
    Height: The height of a rectangle

    Method:
    __init__(width, height): width and height of a rectangle

    Raise:
        TypeError:
                i) If width is not Integer
                ii) If height is not integer
        ValueError:
                i) If width is less than 0
                ii) If height is less than 0

    """
    def __init__(self, width=0, height=0):
        """ Initializes the width and height
        with optional size
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ Getter property for width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter property to set the value of width"""

        if type(value) is not int:
            raise TypeError("width must be an integer")

        elif value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """ Getter property for height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter property to set the value of height"""

        if type(value) is not int:
            raise TypeError("height must be an integer")

        elif value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
