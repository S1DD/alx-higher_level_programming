#!/usr/bin/python3

"""
Module add_integer
Adds two integers together

"""


def add_integer(a, b):

    """
    Returns the addition of a and b,
    or error if a and b are not integers or floats
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")

    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return a + b
