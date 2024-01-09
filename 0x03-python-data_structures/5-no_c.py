#!/usr/bin/python3
def no_c(my_string):
    text = ""
    for k in my_string:
        if k != 'C' and k != 'c':
            text += k
    return text
