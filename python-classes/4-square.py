#!/usr/bin/python3
"""Create a square"""


class Square:
    """Creating multiple functions and instances
    """
    def __init__(self):
        self.__size = None

    def __int__(self, size):
        self.__size = size

    def area(self):
        return self.__size**2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
