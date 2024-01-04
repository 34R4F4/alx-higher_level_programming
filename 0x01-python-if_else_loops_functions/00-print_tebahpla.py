#!/usr/bin/python3
def uppercase(str):
    for char in str:
        c = ord(char)
        if c in range(97, 123):
            c -= 32
        print("{:c}".format(c), end="")
    print("")
