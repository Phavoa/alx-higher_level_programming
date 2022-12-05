#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    for i in range(len(my_list)):
        if my_list[i] == idx:
            my_list[i + 1] = element
            return (my_lisit)
