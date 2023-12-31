#!/usr/bin/python3
"""Create a function that adds 2 integers"""


def add_integer(a, b=98):
    """Define a function that adds 2 integers"""

    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    if type(a) == float:
        int(a)
    if type(b) == float:
        int(b)
    return int(a + b)
