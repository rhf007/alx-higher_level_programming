#!/usr/bin/python3
"""module for checking on instances"""


def is_kind_of_class(obj, a_class):
    """
    check if if the object is an instance of, or if the object is an instance
    of a class that inherited from, the specified class

    Args:
        obj: object to be checked
        a_class: class to check if obj is from

    Returns:
        True if it is, False otherwise
    """
    if isinstance(obj, a_class):
        return True
    return False
