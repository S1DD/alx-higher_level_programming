#!/usr/bin/python3

""" Defines a Sqaure class """

class Sqaure:
    """ Represents a square """
    def __init__(self,size=0):
        """ Initializes a new sqaure

            Args:
                 size (int): Size of the square

        """
        if size not isstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
