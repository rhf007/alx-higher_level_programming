#!/usr/bin/python3
"""testing module for models/base.py"""


import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """test class for the base model"""
    def setUp(self):
        """setup method"""
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        """teardown method"""
        pass

    def test_id(self):
        """testing an assigned id value"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(None)
        self.assertEqual(b2.id, 2)
        b3 = Base(-1)
        self.assertEqual(b3.id, -1)
        b4 = Base(8)
        self.assertEqual(b4.id, 8)

    def test_to_json_string(self):
        """testing from python to json"""
        jsonstr = Base.to_json_string(None)
        self.assertEqual(jsonstr, '[]')
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        jsonstr = json.dumps([dictionary])
        jsonlstdict = r1.to_json_string([dictionary])
        self.assertTrue(jsonstr == jsonlstdict)

    def test_save_to_file(self):
        """testing saving to a file"""
        import os
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 105)

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        try:
            os.remove("Rectangle.json")
        except Exception:
            pass
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        r3 = Rectangle(2, 4)
        Rectangle.save_to_file([r3])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 52)

        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        try:
            os.remove("Square.json")
        except Exception:
            pass
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        r4 = Square(1)
        Square.save_to_file([r2])
        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), 38)

    def test_from_json_string(self):
        """testing from josn to python"""
        list_input = [{'id': 89, 'width': 10, 'height': 4}, {'id': 7,
                      'width': 1, 'height': 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertTrue(list_input == list_output)

        in2 = []
        json2 = Rectangle.to_json_string(in2)
        out2 = Rectangle.from_json_string(json2)
        self.assertTrue(in2 == out2)

        # couldnt do these two like the ones above
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])

    def test_create(self):
        """testing create function"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertFalse(r1 == r2)
        self.assertFalse(r1 is r2)
        self.assertEqual(str(r1), str(r2))

    def test_load_from_file(self):
        """testing loading from a file"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_input = [r1, r2]
        Rectangle.save_to_file(list_input)
        list_output = Rectangle.load_from_file()
        self.assertNotEqual(id(list_input[0]), id(list_output[0]))
        self.assertEqual(str(list_input[0]), str(list_output[0]))
        self.assertNotEqual(id(list_input[1]), id(list_output[1]))
        self.assertEqual(str(list_input[1]), str(list_output[1]))

        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_s_input = [s1, s2]
        Square.save_to_file(list_s_input)
        list_s_output = Square.load_from_file()
        self.assertNotEqual(id(list_s_input[0]), id(list_s_output[0]))
        self.assertEqual(str(list_s_input[0]), str(list_s_output[0]))
        self.assertNotEqual(id(list_s_input[1]), id(list_s_output[1]))
        self.assertEqual(str(list_s_input[1]), str(list_s_output[1]))


if __name__ == "__main__":
    unittest.main()
