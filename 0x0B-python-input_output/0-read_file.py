#!/usr/bin/python3

"""
0-read_file module
"""


def read_file(filename=""):
    """
    read_file - reads a text file (UTF8) and print its contents to stdout.
    
    Args:
        filename : Name of the file to be read.
    """
    with open(filename, "r", encoding="UTF-8") as f:
        for line in f:
            print(line, end="")
