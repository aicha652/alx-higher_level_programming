#!/usr/bin/python3
"""Create a  function that appends a string at the end
of a text file (UTF8) and returns the number of characters added"""


def append_write(filename="", text=""):
    """Define a function"""

    with open(filename, 'a') as f:
        content = f.write(text)
        return content
