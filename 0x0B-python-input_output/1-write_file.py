#!/usr/bin/python3
"""write file module"""


def write_file(filename="", text=""):
    """write file function

    Args:
        filename: file name
        text: text to write in the file
    """
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(text)
