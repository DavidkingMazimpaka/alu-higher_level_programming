#!/usr/bin/python3
"""
advanced task, attribute to be added
"""


def add_attribute(cls, attribute, value):
    """function that handle if we can't set an attribute
    Args:
        attribute (any): attribute name
        value (any): value for the attribute
    Returns:
        Nothing
        :param value:
        :param attribute:
        :param cls:
    """
    if not hasattr(cls, '__dict__'):
        raise TypeError("can't add new attribute")
    else:
        setattr(cls, attribute, value)
