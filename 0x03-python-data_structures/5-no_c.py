#!/usr/bin/python3

def no_c(my_string):
    mod_str = ''
    for i in my_string:
        if i != 'c' and i != 'C':
            mod_str += i
            return (mod_str)
        
