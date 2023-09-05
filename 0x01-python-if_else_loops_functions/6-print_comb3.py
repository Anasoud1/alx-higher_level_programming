#!/usr/bin/python3
j = 0
i = 0
while i < 8:
    j = 0
    while j < 10:
        if j == 0:
            j = i + 1
        print("{}{}, ".format(i, j), end="")
        j += 1
    i += 1
j -= 1
print("{}{}".format(i, j))
