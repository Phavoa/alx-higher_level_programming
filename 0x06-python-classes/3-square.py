#!/usr/bin/python3
""" Create a class named square """

class Square:
    """ Define init function """
    def __init__(self, size=0):
        """ Initialize size as a privant instance """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    """ defines area function """
    def area(self):
        """ returns area """
        return self.__size ** 2
