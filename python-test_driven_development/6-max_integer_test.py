#!/usr/bin/python3
"""
a function to write unittests
"""


def max_integer(list=[]):
    """
    returning the method with list parameter
    :param list:
    :return:
    """
    if list is None:
        list = []
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
