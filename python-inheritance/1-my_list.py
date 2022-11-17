#!/usr/bin/python3
"""
Define class Mylist
"""


class MyList(list):
    """
    function print_sorted
    """
    def print_sorted(self):
        """
        method print_sorted
        :return:
        """
        print(sorted(self))
