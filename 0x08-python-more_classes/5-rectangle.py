#!/usr/bin/python3
"""
Defines a Rectangle class.
"""


class Rectangle:
    """
    Defines a rectangle class defined by width and height
    """

    def __init__(self, height, width):
        """Initializes a Rectangle instance.

        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.height = height
        self.width = width

    def __str__(self):
        """Returns an informal and nicely printable string representation
        of a Rectangle instance, filled with the '#' character."""
        if self.__height == 0 or self.__width == 0:
            return ''

        rec_str = ''
        for i in range(self.__height):
            for j in range(self.__width):
                rec_str += '#'
            rec_str += '\n'
        return rec_str[:-1]

    def __repr__(self):
        """Prints the string representation of the rectangle
        to be able to recreate a new instance using eval()"""
        return eval(repr(self))

    def __del__(self):
        """Deletes a rectangle instance"""
        print("Bye rectangle...")

    @property
    def width(self):
        """Retrieves the width of a Rectangle instance."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of a Rectangle instance

        Args:
            value: value of the width, must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("width must be a integer")
        elif value < 0:
            raise ValueError("width must be >=0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of a Rectangle instance."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of a Rectangle instance

        Args:
            value: value of the height, must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of a Rectangle instance

        Returns:
                Area of the rectangle, given by height * width
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of a Rectangle instance

        Returns:
                Perimeter of the rectangle, given by 2 * (height + width)
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        perimeter = 2 * (self.__height + self.__width)
        return perimeter
