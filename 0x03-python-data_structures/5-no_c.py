#!/usr/bin/python3
def no_c(my_string):
    newstring = ''
    for char in my_string:
        if char != chr(99) and char != chr(67):
            newstring += char
    return (newstring)
