#!/usr/bin/python3
"""
Inherits BaseGeometry class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Inherits from Rectangle.
    """

    def __init__(self, size):
        """
        init method set the value size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Area of Square
        """
        return self.__size ** 2

    def __str__(self):
        """
        returns string size
        :return:
        """
        return str("[Square] {}/{}".format(self.__size, self.__size))
