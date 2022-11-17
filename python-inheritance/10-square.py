#!/usr/bin/python3
"""
inherited 9-rectangle
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    class Square inherit Rectangle
    """
    def __init__(self, size):
        """
        method init
        :param size:
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
