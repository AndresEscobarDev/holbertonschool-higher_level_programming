#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in i:
            if i.index(j) == len(i) - 1:
                print("{}".format(j))
            else:
                print("{}".format(j), end=" ")
