#!/usr/bin/python3
"""Module for [print_square] Method.

Attributes:
    print_square: function that prints a square with the character #.
"""


def print_square(size):
    """Prints a square with the character #.

    Args:
        size (int): the size length of the square.

    Raises:
        TypeError: If size is not an integer or float less than 0.
        ValueError: If size is less than 0.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        print("#" * size)

