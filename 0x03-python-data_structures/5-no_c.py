#!/usr/bin/python3

def no_c(my_string):
    mod_str = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(mod_str))
