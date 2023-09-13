#!/usr/bin/python3
"""
8-class_to_json module
"""



def class_to_json(obj):
    """
        returns dictionary representation with simple 
        data structure for JSON serialization of an object:
    """
    return obj.__dict__
