#!/usr/bin/python3
"""
Define class Rectangle
"""


class Rectangle:

    number_of_instances = 0

    """ Rectangle """
    def __init__(self, width=0, height=0):
        """ initialize width and height  """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
    @property
    def height(self):
        """ height getter """
        return self.__height


    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value


    def area(self):
        """ Calculate and return the area of the rectangle """
        return self.__width * self.__height


    def perimeter(self):
        """ Calculate and return the perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)


    def __str__(self):
        """ return rectangle representation """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            for i in range(self.__height):
                return ("#" * self.__width + '\n') * self.__height

    def __repr__(self):
        """ Return a string repr """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ del """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
