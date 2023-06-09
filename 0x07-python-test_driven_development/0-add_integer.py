#!/usr/bin/python3
"""
add_integer module
Provides a function to add two numbers.
"""


def add_integer(a, b=98):
    """
     Returns the sum of two numbers.

    Args:
        a (int or float): The first number.
        b (int or float, optional): The second number. Defaults to 98.

    Raises:
        TypeError: If `a` or `b` is not an integer or float.

    Returns:

    """
    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')

    return (int(a) + int(b))
