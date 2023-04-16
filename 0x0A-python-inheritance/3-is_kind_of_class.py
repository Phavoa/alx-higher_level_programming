#!/usr/bin/python3
"""
3-is_kind_of_class module
"""


def is_kind_of_class(obj, a_class):
     """Returns True if obj is an instance of, or if obj
     is an instance of a class that inherited from, a_class; otherwise False."""
    return isinstance(obj, a_class)
