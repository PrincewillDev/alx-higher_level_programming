#!/usr/bin/python3

"""
This module creates a function that appends a string
at the end of a text file
and returns the number of text written
"""


def append_write(filename="", text=""):
    """
    This function appends a string
    at the end of a text file
    and returns the number of text written

    Parameters:
    filename: name of file to append to

    text: text to be appended

    Return:
    Number of characters appended
    """
    with open(filename, 'a', encoding="UTF-8") as text_file:
        file = text_file.write(text)
    return file
