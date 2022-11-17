#!/usr/bin/python3
"""
Class Definition
"""


class LockedClass:
    pass


class LockedClass:
    """
    class is locked
    """

    global first_name
    try:
        first_name = LockedClass()
    except AttributeError:
        print(f"{LockedClass}  object has no attribute {first_name}")
