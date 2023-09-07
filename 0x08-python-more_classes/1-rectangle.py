#!/usr/bin/python3
"""
Define a class named Rectangle
"""
class Rectangle:
    """
    Initialize the class with width and height parameters
    """
    def __init__(self, width=0, height=0):
        """
        Set the initial width and height attributes
        """
        self.width = width
        self.height = height

    """
    Define a property for the width attribute
    """
    @property
    def width(self):
        """
        Retrieve and return the value of the private attribute __width
        """
        return self.__width

    """
    Define a setter for the width attribute
    """
    @width.setter
    def width(self, value):
        """
        Check if value is not an integer
        """
        if type(value) is not int:
            """
            Raise a TypeError with an error message
            """
            raise TypeError("width must be an integer")
        """
        Check if the provided value is less than 0
        """
        elif value < 0:
            """
            Raise a ValueError with an error message
            """
            raise ValueError("width must be >= 0")
        else:
            """
            Set the private attribute __width to value
            """
            self.__width = value

    """
    Define a property for the height attribute
    """
    @property
    def height(self):
        """
        Retrieve and return the value of the private attribute __height
        """
        return self.__height

    """
    Define a setter for the height attribute
    """
    @height.setter
    def height(self, value):
        """
        Check if value is not an integer
        """
        if type(value) is not int:
            """
            Raise a TypeError with an error message
            """
            raise TypeError("height must be an integer")
        """
        Check if the value is less than 0
        """
        elif value < 0:
            """
            Raise a ValueError with an error message
            """
            raise ValueError("height must be >= 0")
        else:
            """
            Set the private attribute __height to the provided value
            """
            self.__height = value
