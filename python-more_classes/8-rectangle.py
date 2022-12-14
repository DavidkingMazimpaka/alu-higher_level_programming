#!/usr/bin/python3
"""
create a rectangle class
"""


class Rectangle:
    """
    create rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        init width and height
        :param width:
        :param height:
        """
        self.width = width
        self.height = height
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
        return "Rectangle ({}, {})".format(
            eval(str(self.width)), eval(str(self.height)))

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2*(self.width + self.height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        instantiate static methods with 2 parameters
        :param rect_1:
        :param rect_2:
        :return:
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
