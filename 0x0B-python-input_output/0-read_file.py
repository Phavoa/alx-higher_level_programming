#!/usr/bin/python3
"""
0-read_file module
"""


def read_file(filename=""):
    """
    read_file - reads a text file (UTF8) and prints it to stdout
    Args:
        filename: name of the file to be read
    """
    with open(filename, "r", encoding="UTF-8") as f:
        data = f.read()
        print(data, end="")
