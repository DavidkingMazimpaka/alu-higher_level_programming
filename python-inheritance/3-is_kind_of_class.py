#!/usr/bin/python3
"""
func is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    method is_kind_of_class
    :param obj:
    :param a_class:
    :return:
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
