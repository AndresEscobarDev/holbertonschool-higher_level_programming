#!/usr/bin/python3
"""Module Matrix-Divided"""


def matrix_divided(m, div):
    """ Function that divides all elements of a matrix."""
    s = "matrix must be a matrix (list of lists) of integers/floats"
    if type(m) != list or len(m) == 0 or type(m[0]) != list:
        raise TypeError(s)
    l = len(m[0])
    if l == 0:
        raise TypeError(s)
    for i in m:
        if type(i) != list:
            raise TypeError(s)
        if len(i) != l:
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if type(j) != float and type(j) != int:
                raise TypeError(s)
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), m))
