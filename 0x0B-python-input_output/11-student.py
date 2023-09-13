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

        """
        if attrs is None:
            return self.__dict__
	dic = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                dic[key] = value
        return dic

    def reload_from_json(self, json):
        """load from json"""
        for key, value in json.items():
            setattr(self, key, value)
