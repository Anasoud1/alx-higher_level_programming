#!/usr/bin/python3
'''Module for matrix_divided method'''


def matrix_divided(matrix, div):
    '''function that divides all elements of a matrix
        Args:
            matrix : matrix
            div: number to divide
        Return: matrix after dividing each element
    '''
    i = 0
    k = 0
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists)"
                        "of integers/floats")
    for li in matrix:
        i += 1
        if not isinstance(li, list):
            raise TypeError("matrix must be a matrix (list of lists)"
                                "integers/floats")
        for j in li:
            if type(j) not in (int, float):
                raise TypeError("matrix must be a matrix (list of lists)"
                "of integers/floats")
    while k + 1 != i:
        if len(matrix[k]) != len(matrix[k + 1]):
            raise TypeError("Each row of the matrix must have the"
            "same size")
        k += 1
    if type(div) not in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    new = []
    for li in matrix:
        for i in li:
            new.append(round(i / div, 2))
        new_matrix.append(new)
        del new
        new = []
    return new_matrix
