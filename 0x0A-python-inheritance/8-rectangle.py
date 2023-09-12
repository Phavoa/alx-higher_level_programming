#!/usr/bin/python3
"""
8-rectangle module
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
""" import 7-base_geometry """

class Rectangle(BaseGeometry):

    """A representation of a rectangle"""
    def __init__(self, width, height):
        """validating of the integer"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        """instantiation of the rectangle"""
        self.__width = width
        self.__height = height
