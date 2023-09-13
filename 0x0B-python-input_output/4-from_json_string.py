#!/usr/bin/python3
"""from JSON module"""


import json


def from_json_string(my_str):
    """from JSON function

    Args:
        my_str: JSON

    Returns:
        string
    """
    return json.loads(my_str)
