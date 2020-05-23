#!/usr/bin/python3
"""Module Matrix-Mul"""


def matrix_mul(m_a, m_b):
    """function that multiplies 2 matrices"""
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")
    if len(m_a) and not all(type(i) == list for i in m_a):
        raise TypeError("m_a must be a list of lists")
    if len(m_b) and not all(type(i) == list for i in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for i in m_a:
        if not all(type(j) in (int, float) for j in i):
            raise TypeError("m_a should contain only integers or floats")
    for i in m_b:
        if not all(type(j) in [int, float] for j in i):
            raise TypeError("m_b should contain only integers or floats")
    l1 = len(m_a[0])
    l2 = len(m_b[0])
    if not all(len(i) == l1 for i in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(i) == l2 for i in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    new = []
    for i in range(len(m_b[0])):
        new.append([])
        for j in range(len(m_b)):
            new[i].append(0)
    for i in range(len(m_b)):
        for j in range(len(m_b[i])):
            new[j][i] = m_b[i][j]
    result = []
    r = 0
    for row in range(len(m_a)):
        result.append([])
        for j in range(len(new)):
            for i in range(len(new[row])):
                r += m_a[row][i] * new[j][i]
            result[row].append(r)
            r = 0
    return result
