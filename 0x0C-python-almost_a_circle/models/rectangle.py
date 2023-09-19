#!/usr/bin/python3
"""
rectangle module
"""

from models.base import Base

class Rectangle(Base):
    """A class representing a Rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a rectangle instance.

            Args:
                width (int): The width of the rectangle.
                height (int): The height of the rectangle.
                x (int): The x position.
                y (int): The y position.
                id (int): An object id.
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ get width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set the width of the rectangle """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value


    @property
    def height(self):
        """ Get the height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ Set the height of the rectangle """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value


    @property
    def x(self):
        """ Get the x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Set the x """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value


    @property
    def y(self):
        """ Get the y """
        return self.__y

    @y.setter
    def y(self, value):
        """ Set the y """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        return area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """ print the rectangle with '#' characters."""
        for i in range(self.__y):
            print()
        for j in range(self.__height):
            for x in range(self.x):
                print(' ', end='')
            for k in range(self.width):
                print("#", end='')
            print()

    def __str__(self):
        """
            returns a string representation of the rectangle
        """
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id,
            self.__x, self.__y, self.__width, self.__height)

    def update(self, *args):
        """
        Update the attributes of the rectangle using *args
        """
        attributes = ["id", "width", "height", "x", "y"]
        for i in range(len(args)):
            if i < len(attributes):
                setattr(self, attributes[i], args[i])