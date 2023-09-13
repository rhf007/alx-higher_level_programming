#!/usr/bin/python3
"""write to JSON file module"""


import json


def save_to_json_file(my_obj, filename):
    """write to JSON file function

    Args:
        my_obj: converted to JSON
        filename: file to write to

    Returns:
        write result
    """
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(json.dumps(my_obj))
