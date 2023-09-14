#!/usr/bin/python3
""" 9-rectangle module """

BaseGeometry = __import__('7-base_geometry').BaseGeometry
""" import 7-base_geometry """

class Rectangle(BaseGeometry):

    """A representation of a rectangle"""

    def __init__(self, width, height):
         """Instantiation of the rectangle.

        Args:
            width (int): The width of the Rectangle.
            height (int): The height of the Rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """ __str__ string representation of the rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
