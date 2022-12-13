#!/usr/bin/python3
""" function that prints a square of #"""


def print_square(size):
    """
    a function with a parameter
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
