#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    add = 0
    num = len(argv)
    if num == 1:
        print("0")
    else:
        for i in range(1, num):
            add = add + int(argv[i])
        print("{}".format(add))
