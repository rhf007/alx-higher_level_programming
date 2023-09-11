#!/usr/bin/python3
"""module to check inheritance"""


def inherits_from(obj, a_class):
    """
    Check for inheritance

    Args:
        obj: object to check
        a_class: check if object is instance of another class inheriting from

    Returns:
        True if it is, false otherwise
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
