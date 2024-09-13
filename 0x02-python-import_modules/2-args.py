#!/usr/bin/python3

if __name__ == "__main__":
     """Print the number of and list of arguments."""
    import sys

    n = len(sys.argv) - 1
    if n == 0:
        print("0 arguments.")
    elif n == 1:
        print("1 argument.")
    else:
        print("{} arguments:".format(n))

    if n >= 1:
        i = 0
        for arg in sys.argv:
            if i != 0:
                print("{}: {}".format(i, arg))
            i += 1
