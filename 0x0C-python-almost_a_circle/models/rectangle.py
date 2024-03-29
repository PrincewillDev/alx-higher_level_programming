#!/usr/bin/python3
from models.base import Base

"""
This module creates a rectangle class
that inherits the Base class from
Base Module.

Class:
    Rectangle: This class represents rectangle
"""


class Rectangle(Base):
    """
    This class represents a rectangle

    Attribute:
        __width: private instance attribute that represent
        the width of the Rectangle class

        __height: private instance attribute that represent
        the height of the Rectangle class

        __x: private instance attribute that represent
        the X axis of the Rectangle class

        __y: private instance attribute that represent
        the Y axis of the Rectangle class

    Method:
        None

    Property:
        width: This is a getter and setter property that returns
        the private instance attribute <__width> and also set it

        height: This is a getter and setter property that returns
        the private instance attribute <__height> and also set it

        x: This is a getter and setter property that returns
        the private instance attribute <__x> and also set it

        y: This is a getter and setter property that returns
        the private instance attribute <__y> and also set it
    Raises:
        TypeError:
            1, If input is not an integer.

        ValueError:
            1, If 'width' is less than or equal to Zero
            2, If 'height' is less than or equal to Zero
            3, If 'x' is less than zero
            4, If 'y' is less than zero
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(type(width).__name__))
        if value < 0:
            raise ValueError("{} must be  > 0".format())
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(type(width).__name__))
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(type(x).__name__))
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(type(y).__name__))
        self.__y = value
