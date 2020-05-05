#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    l = len(my_list)
    if idx < 0:
        return my_list
    if idx >= l:
        return my_list
    new = my_list.copy()
    new[idx] = element
    return new
