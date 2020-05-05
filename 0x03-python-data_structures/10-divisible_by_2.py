#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    boolList = []

    for i in my_list:
        if i % 2 == 0:
            boolList.append(True)
        else:
            boolList.append(False)
    return boolList
