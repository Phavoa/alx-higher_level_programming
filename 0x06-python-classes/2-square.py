#!/usr/bin/python3
""" Define a class named square """



class Square:
    """ Define __init__ function """
    def __init__(self, size=0):
        """ if conditional statement """
        if type(size) is not int:
            """ raise exception error """
            raise TypeError("size must be an integer")
        elif size < 0:
            """ raise exception error """
            raise ValueError("size must be >= 0")
        else:
            """ Initialize __size of self with size """
            self.__size = size
