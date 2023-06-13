#!/usr/bin/python3

""" Module containing a function that reads file """


def read_file(filename=""):

    """
    Args:
        filename: filename

    Raise
        Exception: no exception raised
    """
    with open(filename, "r", encoding="UTF-8") as f:
        readfile = f.read()
        print(readfile, end="")
