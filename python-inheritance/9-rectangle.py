#!/usr/bin/python3
"""Class Rectangle inherited from BaseGeometry (7-base_geometry.py)
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rect inherits the BaseGeometry
    """

    def __init__(self, width, height):
        """method init
        """
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def area(self):
        """Function to return the area of the rectangle"""
        return self.__height * self.__width

    def __str__(self):
        """Returns [Rectangle] """
        return str("[Rectangle] {}/{}".format(self.__width, self.__height))
