#!/usr/bin/python3
def no_c(my_string):
    text = ""
    for k in  my_string:
        if k != 'C' or k != 'c':
            text += k
    return text
