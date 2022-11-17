#!/usr/bin/python3
"""
module `Int` - that modify two magic methods from int class
"""


class MyInt(int):
    """
    class MyInt - with two methods
    """

    def __eq__(self, value):
        """
        return true is two integers are different
        """
        return int(self) != int(value)

    def __ne__(self, value):
        """
        return false is two integers are equal
        """
        return int(self) == int(value)
