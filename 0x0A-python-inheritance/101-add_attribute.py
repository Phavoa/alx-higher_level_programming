#!/usr/bin/python3
"""
101-add_attribute module
"""


def add_attribute(obj, attrName, attrValue):
    """
    Checks if attrName exists if it does not exist add the new attrribute.
    Args:
        - obj: object or instance of a class
        - attrName: name of new attribute
        - attrValue: value of the new attribute
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attrName, attrValue)
