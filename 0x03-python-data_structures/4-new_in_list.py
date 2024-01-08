#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return None
    list2 = []
    for o in my_list:
        list2.append(o)
    list2[idx] = element
    return list2
