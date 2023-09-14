#!/usr/bin/python3
"""
lookup - returns the list of available attributes and methods of an object
@obj: object
"""

def lookup(obj):
    """ returns the list of object """
    return dir(obj)
