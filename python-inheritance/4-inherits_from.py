#!/usr/bin/python3
"""
inherited func inherits_from
"""


def inherits_from(obj, a_class):
    """
    method inherits_from
    :param obj:
    :param a_class:
    :return:
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
