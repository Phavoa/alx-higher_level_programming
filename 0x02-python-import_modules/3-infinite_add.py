#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    total_sum = 0
    argc = len(argv)
    for i in range(1, argc):
        total_sum += int(argv[i])
    print(total_sum)
