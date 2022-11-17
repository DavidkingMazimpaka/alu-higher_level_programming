#!/usr/bin/python3
"""
function declaration
"""


def is_same_class(obj, a_class):
    """
    method is_same_class
    :param obj:
    :param a_class:
    :return:
    """
    if type(obj) == a_class:
        return True
    else:
        return False
