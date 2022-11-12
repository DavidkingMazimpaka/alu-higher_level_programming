#!/usr/bin/python3
"""Create a square"""


class Square:
    """Creating multiple functions and instances
    """
    def __init__(self):
        self.__size = None

    def __int__(self, size=0):
        self.__size = size

    def area(self):
        return self.__size**2

    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
        """Creating functions from imported property
        """

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
        