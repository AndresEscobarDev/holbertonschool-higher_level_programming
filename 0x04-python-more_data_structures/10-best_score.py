#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    s = ""
    for j in a_dictionary:
        if s == "" or a_dictionary[j] > a_dictionary[s]:
            s = j
    return s
