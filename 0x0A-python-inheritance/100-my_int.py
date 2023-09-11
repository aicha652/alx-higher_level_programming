#!/usr/bin/python3
"""Create a class MyInt that inherits from int"""


class MyInt(int):
    """Define a class"""

    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
