#!/usr/bin/python3
"""
6-load_from_json_file module
"""
import json



def load_from_json_file(filename):
    """
    load_from_json_file - creates an Object from a “JSON file”:
    Args:
        filename: name of the file
    Return: Python object
    """
    with open(filename, "r") as f:
        my_obj = json.load(f)
        return my_obj
