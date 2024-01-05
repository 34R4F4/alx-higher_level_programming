#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argc = len(sys.argv) - 1

    if argc == 0:
        print("{} arguments.".format(argc))
    elif argc == 1:
        print("{} argument:".format(argc))
    else:
        print("{} arguments:".format(argc))

    e = 0
    while e < argc:
        print("{}: {}".format(e + 1, sys.argv[e + 1]))
        e += 1
