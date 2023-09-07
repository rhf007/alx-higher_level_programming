#!/usr/bin/python3
"""text indentation module"""


def text_indentation(text):
    """function that prints a text with 2 new lines after each of these
    characters: ., ? and :

    Args:
        text: text to be indented

    Raises:
        TypeError: text isnt a str
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for i in ".?:":
        text = (i + "\n\n").join([line.strip(" ") for line in text.split(i)])
    print(text, end="")
