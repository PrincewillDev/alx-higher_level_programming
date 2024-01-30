#!/usr/bin/python

"""
This module prints a text with 2 new lines
after each of these characters: ., ? and :

Function:
     text_indentation: prints a text with 2 new lines
after each of these characters: ., ? and :

Raises:
    TypeError:If text is not an str
"""


def text_indentation(text):
    """ 
    Theprints a text with 2 new lines
    after each of these characters: ., ? and :
    """
    current = ""
    if type(text) != str:
        raise TypeError("text must be a string")

    for char in text:
        print(char, end="")
        if char == '.' or char == '?' or char == ':':
            print('\n')
