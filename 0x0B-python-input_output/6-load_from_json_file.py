#!/usr/bin/python3

import json
"""Defines a function that creates an Object from a JSON file"""


def load_from_json_file(filename):
    """Creates an object from a JSON file"""
    with open(filename) as f:
        json.load(f)
