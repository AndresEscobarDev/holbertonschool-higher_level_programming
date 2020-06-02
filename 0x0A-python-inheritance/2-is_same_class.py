#!/usr/bin/python3
""" IsSameClass Module """


def is_same_class(obj, a_class):
    """  function that returns True if the object
    is exactly an instance of the specified class ;
    otherwise False.
    """
    return True if type(obj) == a_class else False
