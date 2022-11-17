#!/usr/bin/python3
"""
Define class BaseGeo
"""


def integer_validator(name, value):
    """
    returns args name and value
    :param name:
    :param value:
    :return:
    """
    if type(value) != int:
        raise TypeError('{} must be an integer'.format(name))
    if value <= 0:
        raise ValueError('{} must be greater than 0'.format(name))


class BaseGeometry:
    """
    class to inherit BaseGeometry
    """
    def area(self):
        """
        returns area
        :return:
        """
        raise Exception('area() is not implemented')


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """
        method init width and height
        :param width:
        :param height:
        """
        integer_validator("width", width)
        integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        return string
        :return:
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """
        method to return area
        :return:
        """
        return self.__width * self.__height


class Square(Rectangle):
    """
    inherited Rec to Square
    """
    def __init__(self, size):
        """
        method init with arg size
        :param size:
        """
        integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """
        built-in method self
        :return:
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
