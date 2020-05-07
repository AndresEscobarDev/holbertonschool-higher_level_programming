#!/usr/bin/python3
def uniq_add(my_list=[]):
    s = 0
    new = list(dict.fromkeys(my_list))
    for i in new:
        s += i
    return s
