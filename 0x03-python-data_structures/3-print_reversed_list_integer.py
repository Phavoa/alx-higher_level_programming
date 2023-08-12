#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in range(len(my_list)):
        i = i - ((i * 2) + 1)
        print("{}".format(my_list[i]))
