#!/usr/bin/python3
def to_uper(character):
    if ord(character) >= 97 and ord(character) <= 122:
        return (ord(character) - 32)
    else:
        return ord(character)


def uppercase(s):
    new = ""
    for character in s:
        new += "%c" % to_uper(character)
    print("{:s}".format(new))
