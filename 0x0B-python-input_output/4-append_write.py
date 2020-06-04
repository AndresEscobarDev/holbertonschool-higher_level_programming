#!/usr/bin/python3
""" AppendWrite Module """


def append_write(filename="", text=""):
    """ Function that appends a string at the
    end of a text file (UTF8) and returns
    the number of characters added
    """
    with open(filename, 'a') as f:
        return f.write(text)
