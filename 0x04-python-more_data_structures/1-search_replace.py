#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return list(map(lambda s: replace if s == search else s, my_list))
