#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        e = 0
        r = 0
        while e < x:
            if isinstance(e, int):
                print("{:d}".format(my_list[e]), end="")
                r = r + 1
            e = e + 1
    except (IndexError, ValueError, TypeError):
        e = e + 1
    finally:
        print()
        return r
