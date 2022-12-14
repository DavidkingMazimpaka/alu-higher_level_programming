#!/usr/bin/python3
"""
Testing max integer function
"""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    class to test integer
    """

    def test_max_integer(self):
        """
        testing function
        :return:
        """
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([5, 2, 3, 4]), 5)
        self.assertAlmostEqual(max_integer([1, 2, 7, 3, 4]), 7)
        self.assertAlmostEqual(max_integer([1, 2, 3, -4]), 3)
        self.assertAlmostEqual(max_integer([4]), 4)
        self.assertAlmostEqual(max_integer([-4]), -4)
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer(), None)
