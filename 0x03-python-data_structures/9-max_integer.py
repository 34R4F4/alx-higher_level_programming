#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max_v = my_list[0]
    for vlaue in my_list:
        if my_list[value] > max_v:
            max_v = my_list[value]
    return max_v
