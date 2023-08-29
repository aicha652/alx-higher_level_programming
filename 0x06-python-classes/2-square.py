#!/usr/bin/python3
"""Create a Square class"""


class Square:

    """A class that defines a Square class

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
                    raise TypeError("size must be an integer")
                elif size < 0:
                    raise ValueError("size must be >= 0")
                else:
                    self._Square__size = size
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
