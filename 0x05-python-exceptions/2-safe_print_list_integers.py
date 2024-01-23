#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        e = 0
        while e < x:
            print("{:d}".format(my_list[e], end=""))
            e = e + 1
    except (IndexError, ValueError, TypeError):
        print("ERROR")
    finally:
        print()
        return e
