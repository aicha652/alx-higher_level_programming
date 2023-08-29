#!/usr/bin/python3
"""Create a Class Square"""


class Square:

    """A class that defines a square"""

    def __init__(self, size=0):

        """__init__ method

        Args:
            size (int): Description of size
        """
        if size is not None:
            try:
                if type(size) is not int:
                    raise TypeError
                if size < 0:
                    raise ValueError
                self._Square__size = size
            except TypeError:
                print("size must be an integer")
            except ValueError:
                print("size must be >= 0")

    def area(self):
        return self._Square__size * self._Square__size
