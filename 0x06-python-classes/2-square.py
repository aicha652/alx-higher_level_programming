#!/usr/bin/python3
"""Create a Square class"""


class Square:

    """A class that defines a Square

    Attributes:
        size (int): Description of size
    """

    def __init__(self, size=0):

        """__init__ method
        Args:
            size (int): Description of size
        """
        if size is not None:
            if type(size) is not int:
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
            self._Square__size = size
