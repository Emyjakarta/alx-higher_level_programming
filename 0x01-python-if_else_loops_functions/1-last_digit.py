#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
z = number % 10
if z > 5:
    print("Last digit of", number, "is", z, "and is greater than 5")
elif z == 0:
    print("Last digit of", number, "is", z, "and is 0")
else:
    print("Last digit of", number, "is", z, "and is less than 6 and not 0")
