#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for i in range(len(matrix)):
        new.append([])
        for j in matrix[i]:
            new[i].append(j ** 2)
    return new
