#!/usr/bin/python3
""" Define a class named square """


class Square:
    """ Define __init__ function """
    def __init__(self, size=0):
        """ Initialize size as a privant instance """
        self.__size = size

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
            """ Initialize size as a privant instance """
            self.__size = value
            
    """ defines area function """
    def area(self):
        """ returns area """
        return self.__size ** 2
