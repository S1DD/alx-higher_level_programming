#!/usr/bin/python3

"""Defines a class MyList"""


class MyList(list):
    """A class that inherits from list"""

    def print_sorted(self):
        """Prints a sorted list"""

        print(sorted(self))
