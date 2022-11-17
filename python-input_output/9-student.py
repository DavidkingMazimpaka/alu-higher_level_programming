#!/usr/bin/python3
"""
class student
"""


class Student:
    """
    class to return init and to_json
    """
    def __init__(self, first_name, last_name, age):
        """
        method init with args
        :param first_name:
        :param last_name:
        :param age:
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        method to return to_json
        :return:
        """
        return self.__dict__
