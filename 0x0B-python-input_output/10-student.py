#!/usr/bin/python3
"""student to json module"""


class Student:
    """student class"""

    def __init__(self, first_name, last_name, age):
        """initialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retreive json

        Args:
	    attrs: some attribute

        Returns:
            new dict if attrs is list of strings, json otherwise
        """
        if attrs is None:
            return self.__dict__
	dic = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                dic[key] = value
        return dic
