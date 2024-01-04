#!/usr/bin/python3
def print_last_digit(number):
    n = 0
    if number < 0:
        n = -number
    else:
        n = number

    while n >= 10:
        n %= 10

    if n == 0:
        print(0, end="")
        return 0
    else:
        print("{:d}".format(n), end="")
        return n
