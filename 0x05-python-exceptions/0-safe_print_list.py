#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        j = 0
        for i in my_list[:x]:
            print("{}".format(i), end="")
            j += 1
        print()
    except IndexError:
        j = 0
        for i in my_list:
            j += 0
            print("{}".format(i), end="")
        print()
    return j
