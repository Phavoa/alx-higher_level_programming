#!/usr/bin/python3
def uppercase(str):
    result = ""
    for i in str:
        upper = ord(i)
        if upper >= 97 and upper <= 122:
            upper = upper - 32
            result += chr(upper)
        else:
            result += chr(upper)
    print(result, end='')
    print("")
