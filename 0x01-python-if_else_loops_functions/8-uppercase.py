#!/usr/bin/python3
def uppercase(str):
    for i in str:
        upper = ord(i)
        if upper >= 97 and upper <= 122:
            upper = upper - 32
        upper = chr(upper)
        print("{}".format(upper), end='')
    print("")
