#!/usr/bin/python3
"""Define a class Square."""

class Sqaure:
    """ Represents a square """
    def __init__(self, size=0):
        """Initializes a new square
         
         Args:
             size (int): Size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ Retutns the current square area."""
        return (self.__size * self.__size)
