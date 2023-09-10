#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for li in matrix:
        for j in li:
            print("{:d}".format(j), end=" ")
        print()
