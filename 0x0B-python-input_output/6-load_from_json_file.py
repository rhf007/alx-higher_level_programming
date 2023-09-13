#!/usr/bin/python3
"""Create object from a JSON file module"""


import json


def load_from_json_file(filename):
    """Create object from a JSON file function

    Args:
        filename: file

    Returns:
        object
    """
    with open(filename, "r", encoding='utf-8') as f:
        return json.load(f)
