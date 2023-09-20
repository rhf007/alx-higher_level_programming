#!/usr/bin/python3
"""module for testing square.py"""


import unittest
from models.base import Base
from models.square import Square
from unittest.mock import patch
from io import StringIO


class TestSquare(unittest.TestCase):
    """test class"""
    def setUp(self):
        """setup method"""
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        """teardown method"""
        pass

    def test_initialize(self):
        """testing initialization and instantiation"""
        s1 = Square(5)
        s2 = Square(2, 2)
        s3 = Square(3, 1, 3)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s2.id, 2)
        self.assertEqual(s3.id, 3)

    def test_exceptions(self):
        """testing exceptions"""
        with self.assertRaises(TypeError):
            s = Square("1")
        with self.assertRaises(TypeError):
            s = Square(1, "2")
        with self.assertRaises(TypeError):
            s = Square(1, 2, "3")
        with self.assertRaises(ValueError):
            s = Square(-1)
        with self.assertRaises(ValueError):
            s = Square(1, -2)
        with self.assertRaises(ValueError):
            s = Square(1, 2, -3)
        with self.assertRaises(ValueError):
            s = Square(0)

    def test_s_area(self):
        """testing area"""
        s1 = Square(5)
        s2 = Square(2, 2)
        s3 = Square(3, 1, 3)
        self.assertEqual(s1.area(), 25)
        self.assertEqual(s2.area(), 4)
        self.assertEqual(s3.area(), 9)

    def test_s_display(self):
        """testing display"""
        s1 = Square(2)
        res = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            s1.display()
            self.assertEqual(str_out.getvalue(), res)
        s1 = Square(4)
        res = "####\n####\n####\n####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            s1.display()
            self.assertEqual(str_out.getvalue(), res)
        s1.size = 5
        res = "#####\n#####\n#####\n#####\n#####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            s1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_s_str(self):
        """testing str"""
        s1 = Square(5)
        s2 = Square(1, 1)
        s3 = Square(3, 4, 5)
        s4 = Square(10, 20, 30, 40)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        self.assertEqual(str(s2), "[Square] (2) 1/0 - 1")
        self.assertEqual(str(s3), "[Square] (3) 4/5 - 3")
        self.assertEqual(str(s4), "[Square] (40) 20/30 - 10")

    def test_s_update_all(self):
        """testing update with and without kwargs"""
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        s1.update(10)
        self.assertEqual(str(s1), "[Square] (10) 0/0 - 5")
        s1.update(1, 2)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 2")
        s1.update(1, 2, 3)
        self.assertEqual(str(s1), "[Square] (1) 3/0 - 2")
        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (1) 3/4 - 2")
        s1.update(x=12)
        self.assertEqual(str(s1), "[Square] (1) 12/4 - 2")
        s1.update(size=7, y=1)
        self.assertEqual(str(s1), "[Square] (1) 12/1 - 7")
        s1.update(size=7, id=89, y=1)
        self.assertEqual(str(s1), "[Square] (89) 12/1 - 7")

    def test_s_to_dictionary(self):
        """testing dictionary representation"""
        s = Square(10, 2, 1)
        self.assertEqual(str(s), "[Square] (1) 2/1 - 10")
        s_dictionary = s.to_dictionary()
        s2 = Square(1, 1)
        s2.update(**s_dictionary)
        self.assertEqual(str(s), str(s2))
        self.assertNotEqual(s, s2)
        s3 = Square(9, 2, 3, 4)
        d = {'x': 2, 'y': 3, 'size': 9, 'id': 4}
        self.assertEqual(s3.to_dictionary(), d)


if __name__ == "__main__":
    unittest.main()
