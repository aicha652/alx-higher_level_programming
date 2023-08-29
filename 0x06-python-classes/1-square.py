#!/usr/bin/python3
"""Create a square class"""


class Square:

    """A class that define a square class"""
    size = None

    def __init__(self, new_size):

        """Create __init__ method"""

        if new_size is not None:
            self._Square__size = new_size


s = Square("3")
s.size
