#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
operation = number % 10
if number < 0:
    operation = number % -10
print("Last digit of " + str(number) + " is " + str(operation), end="")
if operation < 6 and operation != 0:
    print(" and is less than 6 and not 0")
elif operation > 5:
    print(" and is greater than 5")
else:
    print(" and is 0")
