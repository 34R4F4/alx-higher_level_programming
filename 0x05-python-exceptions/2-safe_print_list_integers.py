#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    e = 0
    r = 0
    while e < x:
        try:
            print("{:d}".format(my_list[e]), end="")
            r = r + 1
        except (ValueError, TypeError):
            pass
        e = e + 1
    print()
    return r
