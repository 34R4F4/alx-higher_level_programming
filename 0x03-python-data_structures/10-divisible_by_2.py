#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    result = []
    for value in range(len(my_list)):
        if my_list[value] % 2 == 0:
            result[value] == True
        else:
            result[value] == False
    return result
