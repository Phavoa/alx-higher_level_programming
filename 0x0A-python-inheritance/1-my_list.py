#!/usr/bin/pytihon3
class MyList(list):
    """ define public instance method """
    def print_sorted(self):
        """ print sorted list """
        print(sorted(self))
