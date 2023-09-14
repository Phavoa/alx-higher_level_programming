#!/usr/bin/python3
"""
10-square module
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square.
    Inherits from Rectangle.
    """
    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the square (all sides are equal).
        """
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2
