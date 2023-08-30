#!/usr/bin/python3
""" Define a class named square """

class Square:
    """ Define init function """
    def __init__(self, size=0):
        """ conditional statement """
        if type(size) is not int:
            """ raise exception """
            raise TypeError("size must be an integer")
        elif size < 0:
            """ raise exception """
            raise ValueError("size must be >= 0")
        else:
            """ Initialize size as a privant instance """
            self.__size = size
