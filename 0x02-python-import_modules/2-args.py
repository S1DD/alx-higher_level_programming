if __name == "__main__":
    import sys

    n = len(sys.argv) - 1
    if n == 0:
        print("0 arguments.")
    elif n == 1:
        print("1 argument.")
    else:
        print("{} arguments:".format(n))
    for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))