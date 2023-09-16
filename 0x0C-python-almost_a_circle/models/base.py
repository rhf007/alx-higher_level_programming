#!/usr/bin/python3
"""base module"""
import json


class Base:
    """base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON representation"""
        if list_dictionaries is None:
            return "[]"
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """save json to file"""
        filename = "{}.json".format(cls.__name__)
        lst = []
        if list_objs is not None:
            for i in range(len(list_objs)):
                lst.append(cls.to_dictionary(list_objs[i]))
        with open(filename, "w", encoding='utf-8') as f:
            f.write(cls.to_json_string(lst))

    @staticmethod
    def from_json_string(json_string):
        """JSON to python"""
        lst = []
        if json_string is None or json_string == "":
            return []
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """create instance"""
        if cls.__name__ == "Rectangle":
            newinst = cls(1, 1)
        if cls.__name__ == "Square":
            newinst = cls(1)
        newinst.update(**dictionary)
        return newinst

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        from os import path
        filename = "{}.json".format(cls.__name__)
        if path.exists(filename) is False:
            return []

        with open(filename, 'r') as f:
            list_str = f.read()

        list_cls = cls.from_json_string(list_str)
        list_ins = []

        for index in range(len(list_cls)):
            list_ins.append(cls.create(**list_cls[index]))

        return list_ins
