#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers. """


def find_peak(list_of_integers):
    """ Function that finds a peak in
    a list of unsorted integers. """
    if not list_of_integers or list_of_integers == []:
        return None
    left = 0
    right = len(list_of_integers) - 1
    if right == 0 or right == 1:
        return max(list_of_integers)
    mid = int(right / 2)
    if list_of_integers[mid] >= list_of_integers[mid - 1] and\
         list_of_integers[mid] >= list_of_integers[mid + 1]:
        return list_of_integers[mid]
    if list_of_integers[mid] > list_of_integers[mid + 1]:
        return find_peak(list_of_integers[:mid])
    return find_peak(list_of_integers[mid:])
