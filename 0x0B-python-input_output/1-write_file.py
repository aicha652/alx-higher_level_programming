#!/usr/bin/python3
"""function that writes a string to a text file
(UTF8) and returns the number of characters written"""


def write_file(filename="", text=""):
    """Define a function"""

    with open(filename, 'w') as f:
        content = f.write(text)
        return (content)
