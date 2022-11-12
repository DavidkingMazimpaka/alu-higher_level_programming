#!/usr/bin/python3
"""Create a square"""


class Square:
    """Creating a function and instance"""

    def __int__(self, size):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise TypeError('size must be >= 0')
        self.__size = size
