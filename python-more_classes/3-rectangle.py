#!/usr/bin/python3
"""
create a rectangle class
"""


class Rectangle:
    """
        create rectangle
    """
    def __init__(self, width=0, height=0):
        """
        init size with args
        :param width:
        :param height:
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        self.__width = width

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        str_i = ""
        for i in range(self.height):
            for j in range(self.width):
                str_i += "#"
            if i == self.height - 1:
                break
            else:
                str_i += "\n"
        return str_i

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2*(self.width + self.height)
