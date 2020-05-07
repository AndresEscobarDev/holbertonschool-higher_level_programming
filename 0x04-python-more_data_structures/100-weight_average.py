#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list or len(my_list) == 0:
        return 0
    r = 0
    p = 0
    for i in my_list:
        r += i[0] * i[1]
        p += i[1]
    r /= p
    return r
