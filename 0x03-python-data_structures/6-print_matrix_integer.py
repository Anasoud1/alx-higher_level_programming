#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for li in matrix:
        if not li:
            print()
            return None
        for j in range(len(li)):
            if j != len(li) - 1:
                print("{:d}".format(li[j]), end=" ")
            else:
                print("{:d}".format(li[j]))
