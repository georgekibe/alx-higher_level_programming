#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = number % 10
forNegative = 10 - lastDigit
if number > 0 and lastDigit > 5:
    print(f"Last digit of {number} is {lastDigit} and is greater than 5")
elif number > 0 and lastDigit <= 5:
    print(f"Last digit of {number} is {lastDigit} and is less than 6 and not 0")
elif lastDigit == 0:
    print(f"Last digit of {number} is {lastDigit} and is {lastDigit}")
elif number < 0:
    print(f"Last digit of {number} is {-1*forNegative} and is less than 6 and not 0")
