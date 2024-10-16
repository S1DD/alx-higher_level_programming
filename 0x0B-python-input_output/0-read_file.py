#!/usr/bin/python3

def read_file(filename="", encoding="utf-8"):
    """ Reads from a text file and prints
        it to stdout

        Args:
             filename: The file to read
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
