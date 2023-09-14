#!/usr/bin/python3
"""
4-from_json_string module
"""
import json



def from_json_string(my_str):
    """
    from_json_string - returns an object  represented by a JSON string:
    Args:
        my_str: JSON string representation
    Return: Python object (Python data structure)
    """
    return json.loads(my_str)
