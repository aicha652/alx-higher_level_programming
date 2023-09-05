#!/usr/bin/python3
"""Create a function that prints a text with 2 new lines\
        after each of these characters: ., ? and :
"""

def text_indentation(text):
    """function that prints a text with 2 new lines"""

    if type(text) != str:
        raise TypeError("text must be a string")
    text = text.replace(".", ".\n\n")
    text = text.replace(".", "?\n\n")
    text = text.replace(".", ":\n\n")

    lines = text.strip().split('\n\n')
    for i in range(len(lines) - 1):
        print(lines[i].strip())

    if lines:
        print(lines[-1].strip(), end="")
