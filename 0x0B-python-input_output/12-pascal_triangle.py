#!/usr/bin/python3
'''Define pascal_triangle function'''


def pascal_triangle(n):
    ''' returns a list of lists of integers representing the
    Pascal’s triangle of n'''
    li = []
    if n <= 0:
        return li
    for i in range(n):
        new = []
        for j in range(i+1):
            new.append(1)
        li.append(new)

    i = 2
    while i < n:
        j = 1
        while j < i:
            li[i][j] = li[i-1][j-1] + li[i-1][j]
            j += 1
        i += 1
    return li
