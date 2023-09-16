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
            lst.append(json.loads(json_string))
            return lst

    @classmethod
    def create(cls, **dictionary):
        """create instance"""
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            newinst = Rectangle(1, 1)
        elif cls is Square:
            newinst = Square(1)
        else:
            newinst = None
        newinst.update(**dictionary)
        return newinst
