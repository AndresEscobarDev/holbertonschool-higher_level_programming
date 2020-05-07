#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    s = dict()
    for i in a_dictionary:
        s[i] = a_dictionary[i] * 2
    return s
