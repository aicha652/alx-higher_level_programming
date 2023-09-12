#!/usr/bin/python3
"""Create a function that creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """Define function"""

    with open(filename, encoding="utf-8") as f:
        content = f.read()
        return (json.loads(content))
