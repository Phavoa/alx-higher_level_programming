#!/usr/bin/python3
""" square """
from models.rectangle import Rectangle

class Square(Rectangle):
    """ A class representing a square """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square instance.

            Args:
                size (int): The size of the Square.
                x (int): The x podition.
                y (int): The y position.
                id (int): An onject id.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Get the size of the Square """
        return self.width

    @size.setter
    def size(self, value):
        """ Get the size of the Square """
        self.width = value
        self.height = value

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - (size)".format(self.id, self.x,
                    self.y, self.width)

    def update(self, *args, **kwargs):
        if args:
            attributes = ["id", "size", "size", "x", "y"]
            for i in range(len(args)):
                if i < len(attributes):
                    setattr(self, attributes[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)


    def to_dictionary(self):
        return {"id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y}
