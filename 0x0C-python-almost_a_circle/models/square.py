#!/usr/bin/python3
"""square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update square"""
        if args is not None and len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.width = args[i]
                    self.height = args[i]
                elif i == 2:
                    self.x = args[i]
                else:
                    self.y = args[i]
        elif kwargs is not None and len(kwargs) != 0:
            for kwarg in kwargs:
                if kwarg == "id":
                    self.id = kwargs[kwarg]
                elif kwarg == "size":
                    self.width = kwargs[kwarg]
                    self.height = kwargs[kwarg]
                elif kwarg == "x":
                    self.x = kwargs[kwarg]
                else:
                    self.y = kwargs[kwarg]

    def to_dictionary(self):
        """dict representation"""
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}

    def __str__(self):
        """str function for square"""
        return "[Square] ({}) {}/{} - {}"\
               .format(self.id, self.x, self.y, self.width)
