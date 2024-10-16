#!/usr/bin/python3

"""Defines a string to be appended at the end of the file"""


def append_write(filename="", text=""):
    """
    Writes and appends a string to a utf-8 tet file

    Args:
        filename:(str) The name of the text file
        text:(str) The text to be written and appended at the end of the file

        Return: The string to append and the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
