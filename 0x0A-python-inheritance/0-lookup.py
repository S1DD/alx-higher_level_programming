#!/usr/bin/python3

"""Defines an attribute lookup function"""


def lookup(obj):
    """Returns a list of available attributes of an object"""
    return (dir(obj))
