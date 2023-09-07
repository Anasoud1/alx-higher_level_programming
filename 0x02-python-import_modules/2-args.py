#!/usr/bin/python3
import sys
le = len(sys.argv)
if le == 2:
    print("1 argument:")
    print("1: {}".format(sys.argv[1]))
else:
    i = 1
    print("{} arguments{}".format(le - 1, ":" if le != 1 else "."))
    for av in sys.argv[1:]:
        print("{}: {}".format(i, sys.argv[i]))
        i += 1
