#!/usr/bin/python3
"""Create a class with no class or object attribute"""


class LockedClass:
    """
    LockedClass with no class or object attribute
    that prevents the user from dynamically creating new instance
    attributes, except if the new instance attribute is called first_name
    """
    __slots__ = ("first_name")

    def __init__(self, val):
        self.first_name = val
