#!/usr/bin/python3
""" add function """


def add_integer(a, b=98):
    """Add 2 integers

    Args:
        a(int): first number
        b(int): second number
    """
    if not isinstance(a, int) or not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) or not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
