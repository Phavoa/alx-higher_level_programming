#!/usr/bin/python3
"""
100-my_int module
"""


class MyInt(int):
    """
    class MyInt inherits from int
    """
    def __eq__(self, other):
        """
        equal operator to not equal operator.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        not equal operator to equal operator.
        """
        return super().__eq__(other)
