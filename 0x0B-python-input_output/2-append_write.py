#!/usr/bin/python3
"""append module"""


def append_write(filename="", text=""):
    """append function

    Args:
        filename: file
        text: text

    Returns:
        append result
    """
    with open(filename, "a", encoding='utf-8') as f:
        return f.write(text)
