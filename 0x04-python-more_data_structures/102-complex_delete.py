  #!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not a_dictionary:
        return None
    if not value:
        return a_dictionary
    switch = True
    while switch:
        c = 0
        for i, j in a_dictionary.items():
            if j == value:
                del a_dictionary[i]
                break
            if c == len(a_dictionary) - 1:
                switch = False
            c += 1
    return a_dictionary