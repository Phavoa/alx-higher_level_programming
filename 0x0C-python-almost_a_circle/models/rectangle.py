#!/usr/bin/python3
"""
module rectangle
"""
from models.base import Base

class Rectangle(Base):
    """
    Rectangle class that inherits from Base class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initializes a Rectangle object.
        """

        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """
        overriding the __str__
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)


    def validate_integer(self, value, attribute):
        """
         Validates that the value is an integer.

        Args:
            value (int): The value to be validated.
            attribute (str): The name of the attribute being validated.

        Raises:
            TypeError: If the value is not an integer.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(attribute))

    
    def validate_positive(self, value, attribute):
        """
        Validates that the value is a positive integer.

        Args:
            value (int): The value to be validated.
            attribute (str): The name of the attribute being validated.

        Raises:
            ValueError: If the value is not positive (greater than zero).
        """
        if value <= 0:
            raise ValueError("{} must be > 0".format(attribute))

    
    def validate_nonNegative(self, value, attribute):
        """
        Validates that the value is a non-negative integer.

        Args:
            value (int): The value to be validated.
            attribute (str): The name of the attribute being validated.

        Raises:
            ValueError: If the value is negative.
        """
        if value < 0:
            raise ValueError("{} must be >= 0".format(attribute))
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_integer(value, "width")
        self.validate_positive(value, "width")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_integer(value, "height")
        self.validate_positive(value, 'height')
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_integer(value, "x")
        self.validate_nonNegative(value, "x")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_integer(value, "y")
        self.validate_nonNegative(value, "y")
        self.__y = value

    def area(self):
        """
        area
        """
        return self.__width * self.__height

    def display(self):
        """
        display
        """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute
        """
        if args:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
         returns the dictionary representation of a Rectangle.
        """
        return {'id' : self.id, 'width' : self.__width,
                'height' : self.__height, 'x' : self.__x,
                'y' : self.__y}
