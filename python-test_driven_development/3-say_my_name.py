#!/usr/bin/python3
"""
a function that prints a full name
"""


def say_my_name(first_name, last_name=""):
    """
    return both first name and last name
    :param first_name:
    :param last_name:
    :return:
    """
    if type(first_name) != str:
        raise TypeError('first_name must be a string')
    if type(last_name) != str:
        raise TypeError('last_name must be a string')
    print('My name is {} {}'.format(first_name, last_name))
