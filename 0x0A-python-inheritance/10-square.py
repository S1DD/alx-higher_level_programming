#!/usr/bin/python3

Rectangle = __import__('9-rectangle.py').Rectangle
"""Defines a Sqaure class"""


class Square(Rectangle):
    """Represents a Square that inherits from Rectangle"""
    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
    
