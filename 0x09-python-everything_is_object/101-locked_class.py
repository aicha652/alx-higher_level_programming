#!/usr/bin/python3
"""Create a class with no class or object attribute"""


class LockedClass:
    __slots__ = ("first_name")

    def __init__(self, val):
        self.first_name = val
