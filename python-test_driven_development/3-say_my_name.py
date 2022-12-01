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
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print(f"My name is {first_name} {last_name}")
