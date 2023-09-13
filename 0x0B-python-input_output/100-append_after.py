#!/usr/bin/python3
"""
100-append_after module
"""

def append_after(filename="", search_string="", new_string=""):
    """ Function that appends a new line when a string is found

    Args:
        filename: filename
        search_string: string to search
        new_string: string to append

    """
    if filename == "" or search_string == "":
        return

    with open(filename, 'r') as f:
        lines = f.readlines()

    with open(filename, 'w') as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
