#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for li in matrix:
        new.append(list(x ** 2 for x in li))
    return new
