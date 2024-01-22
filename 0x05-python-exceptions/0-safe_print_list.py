#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        e = 0
        while e < x:
            print(my_list[e], end="")
            e = e + 1
    except IndexError:
        None
    finally:
        print()
        return e
