#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    multiples_of_2 = []
    div_by_2 = 2

    for value in range(len(my_list)):
        if value % div_by_2 == 0:
            multiples_of_2.append(True)
        else:
            multiples_of_2.append(False)

    return multiples_of_2
