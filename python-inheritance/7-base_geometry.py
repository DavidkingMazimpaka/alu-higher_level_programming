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
    Class BaseGeometry
    """
    def area(self):
        """
        :returns area
        :return:
        """
        raise Exception('area() is not implemented')
    