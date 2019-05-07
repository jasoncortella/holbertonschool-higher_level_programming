#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lenA = len(tuple_a)
    lenB = len(tuple_b)
    new = ((tuple_a[0] if lenA >= 1 else 0) + (tuple_b[0] if lenB >= 1 else 0),
           (tuple_a[1] if lenA >= 2 else 0) + (tuple_b[1] if lenB >= 2 else 0))
    return new
