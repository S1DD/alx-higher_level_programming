#!/usr/bin/python3

"""Defines a class and inherited class checking function"""


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of a class or a subclass of that class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if the object is an instance of `a_class` or an instance
              of a subclass of `a_class`; otherwise, False.
    """
    if isinstance(obj, a_class):
        return True
    return False
