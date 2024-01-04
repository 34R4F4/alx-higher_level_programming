#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = 0
x = 1
if number < 0:
    n = -number
    x = -1
else:
    n = number

while n >= 10:
    n %= 10
n = n*x
if n == 0:
    print(f"Last digit of {number:d} is {n:d} and is 0")
elif n > 5:
    print(f"Last digit of {number:d} is {n:d} and is greater than 5")
else:
    print(f"Last digit of {number:d} is {n:d} and is less than 6 and not 0")
