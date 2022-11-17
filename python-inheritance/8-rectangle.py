#!/usr/bin/python3
"""
Class Rectangle that inherited from BaseGeometry (7-base_geometry.py)
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


def integer_validator():
    pass


class Rectangle(BaseGeometry):
    """
    class Rectangle
    """
    def __init__(self, width, height):
        """
        method init with args width and height
        :param width:
        :param height:
        """
        super().__init__()
        self.height = height
        integer_validator()
        integer_validator()
        self.__width = width
