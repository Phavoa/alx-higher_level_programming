#!/usr/bin/python3
"""
Define class Rectangle
"""


class Rectangle:

    number_of_instances = 0
    print_symbol = "#"

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
        rect_str = ""
        for i in range(self.__height):
            for j in range(self.width):
                rect_str += str(self.print_symbol)
            rect_str += '\n'
        return rect_str[:-1]

    def __repr__(self):
        """ Return a string repr """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ del """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ bigger_or_equal """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        if rect_1.area() < rect_2.area():
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ square classmethod """
        return cls(size, size)
