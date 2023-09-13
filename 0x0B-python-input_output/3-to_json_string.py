#!/usr/bin/python3
"""to JSON module"""


import json
def to_json_string(my_obj):
    """to JSON function

    Args:
        my_obj: object to convert

    Returns:
    JSON format
    """
    return json.dumps(my_obj)
