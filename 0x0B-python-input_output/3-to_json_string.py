#!/usr/bin/python3

"""
This module creates a function <to_json_string(object)>
that accepts a python object and
serialize it (convert it to json format)

Functions:
    to_json_string - Returns the JSON representation of an object.
"""
import json


def to_json_string(my_obj):
    """
    This functions takes a python object and
    serialize it (convert it to json format)

    Parameter:
    my_obj: Python object to be serialize

    Return: Json formatted string
    """
    json_format = json.dumps(my_obj)

    return json_format
