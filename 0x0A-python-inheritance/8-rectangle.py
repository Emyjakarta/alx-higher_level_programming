#!/usr/bin/python3
"empty class BaseGeometry"


class BaseGeometry:
    "empty class BaseGeometry"
    def area(self):
        "no implementation for method yet"
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        "validates value"
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from
    BaseGeometry (7-base_geometry.py)
    """
    def __init__(self, width, height):
        "initialize the rectangle"
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
