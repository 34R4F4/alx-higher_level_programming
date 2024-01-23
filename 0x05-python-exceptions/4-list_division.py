#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    l = 0
    e = 0
    r = []
    while e < list_length:
        try:
            d = my_list_1[e] / my_list_2[e]
            r.append(d)
            l = l + 1
        except IndexError:
            print("out of range")
            r.append(0)
        except (ValueError, TypeError):
            print("wrong type")
            r.append(0)
        except ZeroDivisionError:
            print("division by 0")
            r.append(0)
        finally:
            e = e + 1
    return r
