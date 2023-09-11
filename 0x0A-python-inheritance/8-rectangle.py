#!/usr/bin/python3
"""Create a class Rectangle that inherits from BaseGeometry"""


class BaseGeometry:
    """Define a class"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Define a class"""

    def __init__(self, width, height):
        """Instantiation with width and height"""

        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
