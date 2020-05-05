#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = tuple_a + tuple_b
    if len(tuple_c) == 1:
        return tuple_c
    if len(tuple_c) == 2:
        if len(tuple_a) == 0 or len(tuple_b) == 0:
            return tuple_c
        else:
            c = (tuple_c[0] + tuple_c[1])
            return c
    if len(tuple_c) == 3:
        if len(tuple_a) == 1:
            c = (tuple_c[0] + tuple_c[1], tuple_c[2])
        else:
            c = (tuple_c[0] + tuple_c[2], tuple_c[1])
        return c
    if len(tuple_c) == 4:
        c = (tuple_c[0] + tuple_c[2], tuple_c[1] + tuple_c[3])
        return c
    return (tuple_c)
