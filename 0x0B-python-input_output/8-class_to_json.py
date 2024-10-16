#!/usr/bin/python3

"""Defines a function that returns a dictionary for JSON serialization"""


def class_to_json(obj):
    """Return the dictionary representation of a simple structure"""
    return obj.__dict__
