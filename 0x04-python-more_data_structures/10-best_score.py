#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    s = None
    for i, j in a_dictionary.items():
        if not s or j > a_dictionary[s]:
            s = i
    return s
