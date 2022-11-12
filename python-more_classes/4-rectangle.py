#!/usr/bin/python3
"""
create a rectangle class
"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """
        init size with 2 args
        :param width:
        :param height:
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        :returns width
        :return:
        """
        return self.__width

    @property
    def height(self):
        """
        returns height
        :return:
        """
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
        """
        init height arg
        :param height:
        :return:
        """
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height

    def __str__(self):
        """
        returns the string strip
        :return:
        """
        strip = ""
        for i in range(self.height):
            for j in range(self.width):
                strip += "#"
            if i == self.height - 1:
                break
            else:
                strip += "\n"
        return strip

    def __repr__(self):
        """
        returns the repr string format
        :return:
        """
        return "Rectangle({}, {})".format(
            eval(str(self.width)), eval(str(self.height)))

    def area(self):
        """
        returns the area of rect
        :return:
        """
        return self.width * self.height

    def perimeter(self):
        """
        returns the perimeter of rectangle
        :return:
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2*(self.width + self.height)
