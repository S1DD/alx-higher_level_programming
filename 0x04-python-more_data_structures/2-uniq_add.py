#!/usr/bin/python3

def uniq_add(my_list=[]):
    total = 0
    uniq = set(my_list)
    for x in uniq:
        total += x
    return total
