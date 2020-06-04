#!/usr/bin/python3
""" NumberOfLines Module """


def number_of_lines(filename=""):
    """ Function that returns the number
    of lines of a text file
    """
    with open(filename, 'r') as f:
        n = 0
        for i in f:
            n += 1
        return n
