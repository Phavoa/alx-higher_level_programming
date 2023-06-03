#!/usr/bin/python3
"""
module add_integer
a and b arguments
returns sum of a and b
"""
def add_integer(a, b=98):
    """
    Returns the sum of two integers.

    >>> add_integer(1, 2)
    3
    >>> add_integer(100, -2)
    98
    >>> add_integer(2)
    100
    >>> add_integer(100.3, -2)
    98

    Raises a TypeError if either argument is not an integer or float.

    >>> add_integer(4, "School")
    Traceback (most recent call last):
        ...
    TypeError: b must be an integer
    >>> add_integer(None)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
