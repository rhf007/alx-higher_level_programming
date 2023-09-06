#!/usr/bin/python3
""" add function """


def add_integer(a, b=98):
    """Add 2 integers

    Args:
        a: first number
        b: second number

    Raises:
        TypeError: a,b not float or int

    Returns:
        sum of a, b
    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
