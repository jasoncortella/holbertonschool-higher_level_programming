#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    abnumber = -number
    flag = 1
else:
    abnumber = number
    flag = 0
lastdigit = abnumber % 10
if flag:
    lastdigit *= -1
if lastdigit > 5:
    str = "greater than 5"
elif lastdigit == 0:
    str = "0"
else:
    str = "less than 6 and not 0"
print("Last digit of", number, "is", lastdigit, "and is " + str)
