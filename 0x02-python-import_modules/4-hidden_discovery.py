#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    for x in dir(hidden_4):
        if x[0] != '_' != x[1]:
            print("{}".format(x))
