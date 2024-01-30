#!/usr/bin/python3

"""
This module prints a square with this character '#'

Function:
    print_square:prints a square with this character '#'

Raises:
    TypeError:If size is not an intger
    ValueError:If size is less than 0
"""


def print_square(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
