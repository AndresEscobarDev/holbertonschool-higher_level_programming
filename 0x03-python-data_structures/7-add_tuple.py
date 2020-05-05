#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = [0, 0]
    b = [0, 0]
    for i in range(len(tuple_a)):
        a[i] = tuple_a[i]
    for i in range(len(tuple_b)):
        b[i] = tuple_b[i]
    return (a[0] + b[0], a[1] + b[1])
