#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
lenght = len(argv)
sum = 0
if lenght == 1:
    lenght -= 1
    print(lenght, "arguments.")
else:
    print(lenght - 1, "argument:")
    for i in range(1, lenght):
        sum += 1
        print("{}: {}".format(sum, argv[i]))
