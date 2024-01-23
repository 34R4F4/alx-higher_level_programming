#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        r = a / b
    except ZeroDivisionError:
        return None
    finally:
        print("{:d}".format(value))
        return r
