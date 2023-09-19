#!/usr/bin/python3

class Base:
    """
    Base implementation
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        init - Initialize a Base instance.
        Args:
            id (int): object id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
