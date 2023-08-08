#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    last_digit = number * -1
    last_digit = last_digit % 10
    last_digit = last_digit * -1
else:
    last_digit = number % 10
output = "Last digit of "
if last_digit > 5:
    print("{}{} is {} and is greater than 5".format(output, number, last_digit))
elif last_digit == 0:
    print("{}{} is {} and is 0".format(output, number, last_digit))
elif last_digit < 6 and last_digit != 0:
    print("{}{} is {} and is less than 6 and not 0".format(output, number, last_digit))

