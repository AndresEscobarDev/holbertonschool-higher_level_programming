#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    l = len(my_list)
    if idx < 0:
        return my_list
    if idx >= l:
        return my_list
    for i in my_list:
        if my_list.index(i) == idx:
            my_list.remove(i)
    return my_list
