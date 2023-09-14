#!/usr/bin/python3
"""
11-square module
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square that inherits from Rectangle.
    """
    def __init__(self, size):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the square (all sides are equal).
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """
        str - returns square description
        """
        return str("[Square] {}/{}".format(self.__size, self.__size))
