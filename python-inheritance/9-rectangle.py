#!/usr/bin/python3
"""
Define class BaseGeo
"""


def integer_validator(name, value):
    if type(value) != int:
        raise TypeError('{} must be an integer'.format(name))
    if value <= 0:
        raise ValueError('{} must be greater than 0'.format(name))


class BaseGeometry:
    """
    Class to inherit BaseGeometry
    """
    def area(self):
        raise Exception('area() is not implemented')


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        integer_validator("width", width)
        integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        return self.__width * self.__height
