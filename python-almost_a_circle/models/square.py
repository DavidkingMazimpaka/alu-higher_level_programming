#!/usr/bin/python3
"""
class Square
"""
from .rectangle import Rectangle


class Square(Rectangle):
    """
    creating class Square inheriting parent class Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        init class constructor with initiated parameters
        :param size:
        :param x:
        :param y:
        :param id:
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        returning another attrib
        :return:
        """
        attributes = "[Square] ({}) {}/{} - {}"
        return attributes.format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """
        getter method 'size'
        :return:
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        setter for method 'size'
        :param value:
        :return:
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        assigning parameters to method
        :param args:
        :param kwargs:
        :return:
        """
        if len(args):
            i = 0
            keys_of_attributes = ['id', 'size', 'x', 'y']
            for value in args:
                if i < 4:
                    setattr(self, keys_of_attributes[i], value)
                    i += 1
        else:
            for keys_of_attributes, value in kwargs.items():
                setattr(self, keys_of_attributes, value)

    def to_dictionary(self):
        """
        returning a dictionary attrib
        :return:
        """
        dic = {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
        return dic
