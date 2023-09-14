#!/usr/bin/python3
"""
Contains the inherits_from function
"""


def inherits_from(obj, a_class):
    """
    Inherits From Function

    Checks if an object is an instance of a subclass of a specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of a subclass of 'a_class,'
        otherwise False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
