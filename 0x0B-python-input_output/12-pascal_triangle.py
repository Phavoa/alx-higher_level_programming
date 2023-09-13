#!/usr/bin/python3
"""
12-pascal_triangle module
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers
        Args:
            n (int): number of lists and digits
        Returns: list of lists
    """

    if n <= 0:
        return []

    listList = [[1]]

    for i in range(1, n):
        row = listList[-1]
        new_row = [1]
        for j in range(1, i):
            new_row.append(row[j - 1] + row[j])
        new_row.append(1)
        listList.append(new_row)

    return listList
