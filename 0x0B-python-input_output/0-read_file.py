#!/usr/bin/python3
""" ReadFile Module """


def read_file(filename=""):
    """ Function that reads a text file
    (UTF8) and prints it to stdout
    """
    with open(filename, 'r') as f:
        print(f.read(), end="")
