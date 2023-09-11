#!/usr/bin/python3
"""Module for mylist class"""


class MyList(list):
    """Mylist class that inherits from the list class"""

    def print_sorted(self):
        """Print a sorted list"""
        print(sorted(list(self)))
