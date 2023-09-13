#!/usr/bin/python3
"""class to json module"""


def class_to_json(obj):
    """class to json function

    Args:
        obj: class

    Returns:
        __dict__ attribute of obj
    """
    return vars(obj)
