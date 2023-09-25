#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        ret = fct(*args)
    except (ZeroDivisionError, IndexError) as er:
        sys.stderr.write("Exception: {}\n".format(er))
        return None
    return ret
