#!/usr/bin/python3
upper = 89
lower = 122
for i in range(1, 27):
    if i % 2 != 0:
        print("{}".format(chr(lower)), end="")
        lower -= 2
    elif i % 2 == 0:
        print("{}".format(chr(upper)), end="")
        upper -= 2
