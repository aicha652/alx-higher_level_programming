#!/usr/bin/python3
class Square:

    """A class that defines a Square class"""
    size = None

    def __init__(self, size=0):

        """__init__ method"""
        try:
            if size is not None:
                self._Square__size = size
                if type(size) is not int:
                    raise TypeError
                if size < 0:
                    raise ValueError
        except TypeError as err:
            print("size must be an integer")
        except ValueError as err:
            print("size must be >= 0")
