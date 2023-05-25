#!/usr/bin/python3
"""
0-read_file module
"""


def read_file(filename=""):
    """
    read_file - function to read and print print in stdout
    Args:
        filename: name of the file
    """
    with open(filename, mode= "r", encoding="UTF-8") as f:
        for line in f:
            print(line, end="")
