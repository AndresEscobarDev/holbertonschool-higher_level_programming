#!/usr/bin/python3
""" PascalTriangle Module """


def pascal_triangle(n):
    """ Function that returns a list
    of lists of integers representing
    the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    l = [[1]]
    for i in range(1, n):
        l.append([1])
        for j in range(1, i + 1):
            if j < i:
                l[i].append(l[i - 1][j - 1] + l[i - 1][j])
            else:
                l[i].append(1)
    return l
