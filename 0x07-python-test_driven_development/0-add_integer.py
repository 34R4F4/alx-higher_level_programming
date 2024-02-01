#!/usr/bin/python3
''' Module for add_integer() Method '''


def add_integer(a, b=98):
    ''' Add Two Intgers
    
    Args:
        a: first intger
        b: second intger

    Raises:
        TypeError: if a/b Not int nor float

    Returns:
        SUM a + b
    '''

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

    if __name__ == "__main__":
        import doctest
        doctest.testfile("tests/0-add_integer.txt")
