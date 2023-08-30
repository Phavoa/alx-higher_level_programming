#!/usr/bin/python3
""" Define a class named square """


class Square:
    """ Define __init__ function """
    def __init__(self, size=0):
        """ conditional statement """
        if type(size) is not int:
            """ raise exception error """
            raise TypeError("size must be an integer")
        elif size < 0:
            """ raise exception error """
            raise ValueError("size must be >= 0")
        else:
            """ Initialize size as a privant instance """
            self.__size = size
    """ defines area function """
    def area(self):
        """ returns area """
        return self.__size ** 2
