#!/usr/bin/python3
"""Class Rectangle inherited from BaseGeometry (7-base_geometry.py)"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rect inherits the BaseGeo """

    def __init__(self, width, height):
        """A function that created a rectangle """
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height
