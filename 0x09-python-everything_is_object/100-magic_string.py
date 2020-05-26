#!/usr/bin/python3
"""Function that print Holberton one more time every time that is invoked"""


def magic_string(i = [-1]):
    i[0] += 1
    return "Holberton" + (", Holberton" * i[0])
