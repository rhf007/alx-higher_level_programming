#!/usr/bin/python3
"""square module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square class"""

    def __init__(self, size):
        """square function"""

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """area function"""

        return self.__size ** 2

    def __str__(self):
        """"str func"""
        return "[Square]" + str(self.__size) + "/" + str(self.__size)
