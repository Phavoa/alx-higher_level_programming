#!/usr/bin/python3
"""
2-append_write module
"""


def write_file(filename="", text=""):
    """
    Write a function that appends a string at the end of a
    text file (UTF8) and returns the number of characters added:
    Args:
        filename: name of the file to be written
        text: text to be written
    Return: sum total of number of bytes written.
    """
    with open(filename, mode="a", encoding="UTF-8") as f:
        return (f.write(text))
