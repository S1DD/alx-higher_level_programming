#!/usr/bin/python3
"""
Module text_indentation
Prints a text
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after
    a ., ? and :
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])
    print("{}".format(text), end="")
