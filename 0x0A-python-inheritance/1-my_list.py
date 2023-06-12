#!/usr/bin/pytihon3
class MyList(list):
    """ initialising the object"""
    def __init__(self):
        super().__init__()
    
    """ define public instance method """
    def print_sorted(self):
        """ print sorted list """
        print(sorted(self))
