#!/usr/bin/python3

"""
0-read_file module
"""


def read_file(filename=""):
    """
    Function to read a text file (UTF8) and print its contents to stdout.
    
    Args:
        filename (str): Name of the file to be read.
    """
    with open(filename, mode="r", encoding="UTF-8") as f:
        for line in f:
            print(line, end="")
