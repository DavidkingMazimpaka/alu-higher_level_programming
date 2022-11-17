#!/usr/bin/python3
"""
importing json files
"""


import json


def from_json_string(my_str):
    """ from_json_string
    Args:
        my_str (dict): dictionary
    Returns:
        a JSON
    """
    return json.loads(my_str)
