#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_a = []
    new_b = []

    if len(tuple_a) >= 2:
        new_a = tuple_a[:]
    if len(tuple_b) >= 2:
        new_b = tuple_b[:]
    if len(tuple_a) < 2 or len(tuple_b) < 2:
        if len(tuple_b) == 0:
            new_b.append(0)
            new_b.append(0)
        elif len(tuple_b) < 2:
            new_b.append(tuple_b[0])
            new_b.append(0)
        if len(tuple_a) == 0:
            new_a.append(0)
            new_a.append(0)
        elif len(tuple_a) < 2:
            new_a.append(tuple_a[0])
            new_a.append(0)
    add_tup = (new_a[0] + new_b[0], new_a[1] + new_b[1])
    return add_tup
