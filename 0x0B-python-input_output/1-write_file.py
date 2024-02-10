#!/usr/bin/python3

"""
This module creates a function that writes to a
file and returns the number of text written
"""


def write_file(filename="", text=""):
    """
    This function writes to a file and
    returns the number of text written

    Parameters:
    filename: name of file to be written to

    text: text to be written to the file

    Return:
    Number of text printed
    """

    # open in write mode
    with open(filename, 'w', encoding="UTF-8") as text_file:
        content = text_file.write(text)

    return content
