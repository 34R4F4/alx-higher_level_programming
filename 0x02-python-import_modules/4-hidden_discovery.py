#!/usr/bin/python3
# dir() list defs of module
if __name__ == "__main__":
    import hidden_4

    for deff in dir(hidden_4):
        if deff[:2] != "__":
            print("{}".format(deff))
