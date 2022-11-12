#!/usr/bin/python3
"""
create a rectangle class
"""


class Rectangle:
    """
    instance initialization
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        init width and height
        :param width:
        :param height:
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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
        """
        returns string
        :return:
        """
        strip = ""
        for i in range(self.height):
            for j in range(self.width):
                strip += str(self.print_symbol)
            if i == self.height - 1:
                break
            else:
                strip += "\n"
        return strip

    def __repr__(self):
        """
        returns the repr of width and height
        :return:
        """
        return "Rectangle ({}, {})".format(
            eval(str(self.width)), eval(str(self.height)))

    def __del__(self):
        """
        returns the del of width and height
        :return:
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def area(self):
        """
        returns area of rectangle
        :return:
        """
        return self.width * self.height

    def perimeter(self):
        """
        returns perimeter of rectangle
        :return:
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2*(self.width + self.height)
