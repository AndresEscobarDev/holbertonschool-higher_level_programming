#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    s = 0
    i = 0
    while i < len(roman_string):
        if i + 1 != len(roman_string) and n[roman_string[i]] < \
                n[roman_string[i + 1]]:
            s += n[roman_string[i + 1]] - n[roman_string[i]]
            i += 1
        else:
            s += n[roman_string[i]]
        i += 1
    return s
