#!/usr/bin/python3

"""
This module creates a class that inherits list object
"""


class MyList(list):
    """
    This class inherits the list object

    Attributes:
    None

    Method:
    print_sorted: prints a sorted list

    """
    def print_sorted(self):
        print(sorted(self))
