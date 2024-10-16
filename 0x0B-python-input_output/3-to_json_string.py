#!/usr/bin/python3
import json

"""Defines a string-to-JSON function"""


def to_json_string(my_obj):
    """
    Returns a JSON representation of an object
    """
    return json.dumps(my_obj)
