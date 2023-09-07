#!/usr/bin/python3
import sys
if len(sys.argv) == 1:
    print("0 arguments.")
else:
    i = 1
    print("{} argument:".format(len(sys.argv) - 1))
    for av in sys.argv[1:]:
        print("{}: {}".format(i, sys.argv[i]))
        i += 1
