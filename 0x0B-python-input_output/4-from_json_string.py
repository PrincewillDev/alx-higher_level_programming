#!/usr/bin/python3

"""
This module creates a function <from_json_string(my_str)>
that accepts a json format string and
deserialize it (convert it to python object)

Functions:
    from_json_string: returns an object (Python data structure)
    represented by a JSON string
"""
import json


def from_json_string(my_str):
    """
    This function accepts a json format string and
    deserialize it (convert it to python object)

    Parameter:
    my_str: Json format string

    Return: python object
    """
    py_obj = json.loads(my_str)
    return py_obj
