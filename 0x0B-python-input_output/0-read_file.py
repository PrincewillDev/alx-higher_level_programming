#!/usr/bin/python3

"""
This reads a text file and print
the text file data to stdout
"""


def read_file(filename=""):
    """
    This function takes a text file as input,
    read the text data and print to stdout.

    Parameter:
    filename: the text filename to be read and print
    to stdout
    """
    # open the text file and read
    with open(filename, 'r', encoding="UTF-8") as text_file:
        read_file = text_file.read()

    # Print its content to stdout
    print(read_file, end="")
