#!/usr/bin/python3

import json

"""
This module creates a function <to_json_string(object)>
that accepts a python object and
serialize it (convert it to json format)
"""


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
