#!/usr/bin/python3
"""
method class_to_json
"""


def class_to_json(obj):
    """ class_to_json
    Args:
        obj (any): data
    Returns:
        dictionary
    """
    return obj.__dict__
