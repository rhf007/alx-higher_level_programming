#!/usr/bin/python3
"""module for testing rectangle.py"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from unittest.mock import patch
from io import StringIO


class TestRectangle(unittest.TestCase):
    """testing rectangle.py"""
    def setUp(self):
        """setup method"""
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        """teardown method"""
        pass

    def test_initialize(self):
        """testing initialization and instantiation"""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)

    def test_exceptions(self):
        """testing exceptions"""
        with self.assertRaises(TypeError):
            r4 = Rectangle(1)

        with self.assertRaises(TypeError):
            r5 = Rectangle()

        with self.assertRaises(TypeError):
            r6 = Rectangle(10, "2")

        with self.assertRaises(TypeError):
            r7 = Rectangle(10, 2)
            r7.x = {}

        with self.assertRaises(ValueError):
            r8 = Rectangle(10, 2)
            r8.width = -10

        with self.assertRaises(ValueError):
            r9 = Rectangle(10, 2, 3, -1)

    def test_area(self):
        """testing area"""
        r10 = Rectangle(3, 2)
        r11 = Rectangle(2, 10)
        r12 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r10.area(), 6)
        self.assertEqual(r11.area(), 20)
        self.assertEqual(r12.area(), 56)

    def test_display(self):
        """testing display"""
        r1 = Rectangle(4, 6)
        result = "####\n####\n####\n####\n####\n####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), result)
        r1 = Rectangle(3, 2)
        result = "###\n###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), result)
        r1.x = 4
        result = "    ###\n    ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), result)
        r1.y = 2
        result = "\n\n    ###\n    ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), result)

    def test_str(self):
        """testing str"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")
        r2 = Rectangle(5, 5, 1)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 5/5")

    def test_update(self):
        """testing update"""
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")
        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/10")
        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/3")
        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/10 - 2/3")
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")

    def test_updatekwargs(self):
        """testing update with kwargs"""
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(height=1)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/1")
        r1.update(width=1, x=2)
        self.assertEqual(str(r1), "[Rectangle] (1) 2/10 - 1/1")
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r1), "[Rectangle] (89) 3/1 - 2/1")
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r1), "[Rectangle] (89) 1/3 - 4/2")

    def test_to_dictionary(self):
        """testing dictionary representation"""
        r1 = Rectangle(10, 2, 1, 9)
        self.assertEqual(str(r1), "[Rectangle] (1) 1/9 - 10/2")
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertNotEqual(r1, r2)
        r = Rectangle(1, 2, 3, 4, 5)
        d = {'x': 3, 'y': 4, 'width': 1, 'id': 5, 'height': 2}
        self.assertEqual(r.to_dictionary(), d)


if __name__ == "__main__":
    unittest.main()
