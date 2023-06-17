#!/usr/bin/python3
"""
base module
"""

class Base:
    """
    Base class: Represents the base implementation
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes an instance of the Base class.
        
        Args:
            id (int): The object id (optional)
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
