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

    my_print: Prints the value of square to stdout using #

Properties:
    size: This property is use to get the attribute size (getter)
    size: This property with @size.setter set the value of size (setter)

"""


class Square:

    """
    This class represents a square

    Attributes:
        __size: A private instance attribute (the size of a square)

    Method:
        __init__(size): Initializes the size of a square

        area: Calculates the area of a square

        my_print: Prints the value of square to stdout using #

    Properties:
        size: This property is use to get the attribute size (getter)
        size: This property with @size.setter set the value of size (setter)

    """
    def __init__(self, size=0):

        """
        Initializes the size of a square

        parameter:
            size: The size of a square

        """

        self.__size = size

    @property
    def size(self):

        """
        This property is use retrive the __size private instance attribute
        (Getter)

        """
        return self.__size

    @size.setter
    def size(self, value):

        """
        This property set the value of size (setter)

          parameter:
            value: The value of size

        checks:
            raise TypeError if value is not an integer

            raise ValueError if value is less than 0

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

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
            for r in range(square):
                for c in range(square):
                    print("#", end="")
                print("\n")

