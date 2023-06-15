#!/usr/bin/python3
"""
Module for pascal_triangle method.
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers
        Args:
            n (int): number of lists and digits
        Returns: list of lists
    """
    newlist = []
    for i in range(n):
        row = [1] * (i + 1)
        newlist.append(row)

    for n in range(n):
        for i in range(n - 1):
            newlist[n][i + 1] = sum(newlist[n - 1][i:i + 2])

    return newlist
