#!/usr/bin/python3
"""Create a function that adds a new attribute to
an object if it’s possible"""


def add_attribute(object, name, value):
    """Define a class"""

    if hasattr(object, '__dict__'):
        setattr(object, name, value)
    else:
        raise TypeError("can't add new attribute")
