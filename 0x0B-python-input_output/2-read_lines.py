#!/usr/bin/python3
""" ReadLines Module """


def read_lines(filename="", nb_lines=0):
    """ Function that reads n lines of a
    text file (UTF8) and prints it to stdout
    """
    with open(filename, 'r') as f:
        if nb_lines <= 0:
            print(f.read(), end="")
        else:
            i = 0
            for l in f:
                print(l, end="")
                i += 1
                if i == nb_lines:
                    break
