#!/usr/bin/python3
"""geometry module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle class"""

    def __init__(self, width, height):
        """init method"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """area function"""

        return (self.__width * self.__height)

    def __str__(self):
        '''String representation method.'''
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
