#!/usr/bin/python3
BaseGeometry = __import__("7-base_geometry").BaseGeometry


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
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
