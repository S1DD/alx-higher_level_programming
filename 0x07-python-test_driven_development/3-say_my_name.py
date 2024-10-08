#!/usr/bin/python3

"""
Module 3-say_my_name
Prints name and last name

"""


def say_my_name(first_name, last_name=""):
    """
    Prints a string "My name is <first name> <last name>

    """

    if type(first_name) is not str:
        raise TypeError("first name must be a string")

    if type(last_name) is not str:
        raise TypeError("last name must be a string")

    print("My name is {} {}".format(first_name, last_name))
