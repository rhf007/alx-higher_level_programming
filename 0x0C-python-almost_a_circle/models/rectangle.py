#!/usr/bin/python3
"""rectangle module"""
from models.base import Base


class Rectangle(Base):
    """rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """ setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """rectangle area"""
        return self.__width * self.__height

    def display(self):
        """rectangle display"""
        for i in range(self.__y):
            print()
        for j in range(self.__height):
            print(" " * self.__x, end="")
            for k in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """__str__ for rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}"\
               .format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """update function"""
        if args is not None and len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.__width = args[i]
                elif i == 2:
                    self.__height = args[i]
                elif i == 3:
                    self.__x = args[i]
                else:
                    self.__y = args[i]
        elif kwargs is not None and len(kwargs) != 0:
            for kwarg in kwargs:
                if kwarg == "id":
                    self.id = kwargs[kwarg]
                elif kwarg == "width":
                    self.__width = kwargs[kwarg]
                elif kwarg == "height":
                    self.__height = kwargs[kwarg]
                elif kwarg == "x":
                    self.__x = kwargs[kwarg]
                else:
                    self.__y = kwargs[kwarg]

    def to_dictionary(self):
        """dictionary representation"""
        return {'id': self.id, 'width': self.__width, 'height': self.__height,
                'x': self.__x, 'y': self.__y}
