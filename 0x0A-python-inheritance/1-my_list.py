#!/usr/bin/python3
"""
MyList - child class of list
print_sorted - prints the list, but sorted
@list: parent class
"""

class MyList(list):
    """
    MyList child of list
    """
    def print_sorted(self):
        """
        print_sorted - prints the list, but sorted
        """
        print(sorted(self))
