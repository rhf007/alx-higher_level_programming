#!/usr/bin/python3
"""module to check if the object is exactly an instance of specified class"""


def is_same_class(obj, a_class):
    if type(obj) is a_class:
        return True
    return False
