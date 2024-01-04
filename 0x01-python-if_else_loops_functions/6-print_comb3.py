#!/usr/bin/python3
for t in range(10):
    for o in range(t, 10):
        if t < o:
            if t == 8 and o == 9:
                print(89)
            else:
                print("{:d}{:d}, ".format(t, o), end="")
