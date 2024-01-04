#!/usr/bin/python3
def remove_char_at(str, n):
    string2 = ""
    x = 0
    for char in str:
        if x == n:
            x += 1
        else:
            string2 += char
            x += 1
    return string2
