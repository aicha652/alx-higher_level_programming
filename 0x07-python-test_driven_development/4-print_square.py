#!/usr/bin/python3
"""Create a function that prints a square with the character #"""


def print_square(size):
    """Define a function that prints a square with the character #"""

    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
