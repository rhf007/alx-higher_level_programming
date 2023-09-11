#!/usr/bin/python3
"""module for lookup function"""


def lookup(obj):
    """ function that returns the list of available attributes and methods of
    an object

    Args:
        obj: an  object

    Returns: list
    """
    return (list(dir(obj)))
