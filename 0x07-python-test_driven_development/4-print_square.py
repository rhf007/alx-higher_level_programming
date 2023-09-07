#!/usr/bin/python3
"""Print a square"""


def print_square(size):
    """print a square using #

    Args:
        size: size of the square

    Raises:
        TypeError: if size is not int
        ValueError: size is less than 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
