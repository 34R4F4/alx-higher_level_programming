#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    result = []
    for value in my_list:
        if value % 2 == 0:
            result.append(True)
        else:
            result.append(False)
    return result
