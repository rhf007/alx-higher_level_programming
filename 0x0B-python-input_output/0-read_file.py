#!/usr/bin/python3
"""read file module"""


def read_file(filename=""):
    """read file function

    Args:
        filename: file name
    """

    with open("filename", "r", encoding='utf-8') as f:
        fl = f.read()
