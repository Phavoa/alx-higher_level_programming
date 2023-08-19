#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_number = set(my_list)
    total = 0
    for i in unique_number:
        total += i
    return total
