#!/usr/bin/python3

"""Defines student class"""


class Student:
    def __init__(self, first_name, last_name, age):
        """Initializes a new student
        Args:
             first_name: (str) Name of the student
             last_name: (str) Last nmae of the student
             age: (int) Age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.

        If attrs is a list of strings, represents only those attributes
        included in the list.

        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(el) == str for el in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
