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
        try:
            if size is not None:
                if type(size) is not int:
                    raise TypeError
                if size < 0:
                    raise ValueError
                self._Square__size = size
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
