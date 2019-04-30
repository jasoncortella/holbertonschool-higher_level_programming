#!/usr/bin/python3
for i in range(0, 9 + 1):
    for j in range(i + 1, 9 + 1):
        if i + j < 17:
            print("{}{}, ".format(i, j), end='')
        else:
            print("{}{}".format(i, j))
