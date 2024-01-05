#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argc = len(sys.argv) - 1

    e = 0
    total = 0
    while e < argc:
        arg = int(sys.argv[e + 1])
        total += int(arg)
        e += 1

    print("{}".format(total))
