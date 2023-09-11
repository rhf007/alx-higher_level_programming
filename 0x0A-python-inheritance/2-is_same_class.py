#!/usr/bin/python3
"""module to check if the object is exactly an instance of specified class"""


def is_same_class(obj, a_class):
    """
    Function to check if obj is an instance a specified class

    Args:
        obj: object to check
        a_class: class to check if object is from

    Returns:
        True if it is, flase otherwise
    """
    if type(obj) is a_class:
        return True
    return False
