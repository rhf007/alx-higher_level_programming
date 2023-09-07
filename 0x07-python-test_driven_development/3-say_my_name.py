#!/usr/bin/python3
"""say my name"""


def say_my_name(first_name, last_name=""):
    """Function that prints a full name

    Args:
        first_name (str): first name
        last_name (str): last name
    Raises:
        TypeError: if either first or last names is not a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
