#!/usr/bin/python3
"""
a function that prints a square with the character #.
"""


def print_square(size):
    """
    returning a square of #
    :param size:
    :return:
    """
    if type(size) != int:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    if size == 0:
        return
    else:
        i = 0
        while i < size:
            print('#' * size)
            i += 1


        
