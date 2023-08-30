#!/usr/bin/python3
""" define a class Square """


class Square:
    """ Define __init__ function
    Attributes:
        __size (int): size of the square
        __position(tuple): position of the square in 2D space
    """
    def __init__(self, size=0, position=(0, 0)):
        """ Initialize square of size and position
        Args:
            size (int): size of the square
            position(tuple): position of the square in 2D space
        Returns:
            None
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ returns __size """
        return self.__size

    @size.setter
    def size(self, value):
        """ conditional statement """
        if type(value) is not int:
            """ raise exception error """
            raise TypeError("size must be an integer")
        elif value < 0:
            """ raise exception error """
            raise ValueError("size must be >= 0")
        else:
            """ Initialize size as a private instance """
            self.__size = value

    @property
    def position(self):
        """ return __position """
    
    @position.setter
    def position(self, value):
        """ conditional statement """
        if type(value) is not tuple or len(value) != 2 or \
            type(value[0]) is not int or type(value[1]) is not int or \
            value[0] < 0 or value[1] < 0:
                raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    """ defines area function """
    def area(self):
        """ returns area """
        return self.__size ** 2

    """ defines my_print function """
    def my_print(self):
        """Print the square with # characters."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

    """ define __str__ function """
    def __str__(self):
        """ define the print() representation of a Square """
        square_str = []
        if self.__size == 0:
            square_str.append("")
        else:
            for i in range(self.__position[1]):
                square_str.append("\n")
            for i in range(self.__size - 1):
                square_str.append(" " * self.__position[0] + "#" * self.__size + "\n")
            square_str.append(" " * self.__position[0] + "#" * self.__size)
        return ''.join(square_str)
