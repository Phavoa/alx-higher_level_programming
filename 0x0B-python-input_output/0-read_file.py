#!/usr/bin/python3

""" Module containing a function that reads file """


def read_file(filename=""):
    """
    read_file - reads a text file (UTF8) and print its contents to stdout.
    
    Args:
        filename : filename
    """
    with open(filename, "r", encoding="UTF-8") as f:
        readfile = f.read()
        print(readfile, end="")
