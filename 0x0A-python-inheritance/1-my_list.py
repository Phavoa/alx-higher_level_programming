#!/usr/bin/pytihon3
class MyList(list):

    def print_sorted(self):
        """ print sorted list """
        sorted_list = sorted(self)
        print(sorted_list)
