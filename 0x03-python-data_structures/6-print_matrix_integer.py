#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if len(row) == 0:
            print("")
        for element in range(len(row)):
            print("{:d}".format(row[element]), end="\n" if element == len(row) - 1 else " ")
