#!/usr/bin/python3
for n in range(0, 99):
    print("{:02d}".format(n), end='\n' if n == 99 else ", ")
