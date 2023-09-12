#!/usr/bin/python3
"""geometry module"""


class BaseGeometry:
    """geometry class"""

    def area(self):
        """function that raises an exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validator function

        Args:
            name: name
            value: value to be validated

        Raises:
            TypeError: value not an int
            ValueError: value <= 0
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
