#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    last_digit = number * -1
    last_digit = last_digit % 10
    last_digit = last_digit * -1
else:
    last_digit = number % 10
output = "Last digit of {} is {} and is".format(number, last_digit)

if last_digit > 5:
    print(output, "greater than 5")
elif last_digit == 0:
    print(output, "0")
else:
    print(output, "less than 6 and not 0")
