#!/usr/bin/python3
"""Create a class Student that defines a student"""


class Student:
    """Define a class"""

    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name and age"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Public method that retrieves a dictionary
        representation of a Student instance"""

        if type(attrs) is list:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        return self.__dict__
