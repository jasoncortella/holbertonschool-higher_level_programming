#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 != 0:
        pnum = i - 32
    else:
        pnum = i
    print("{:c}".format(pnum), end='')
