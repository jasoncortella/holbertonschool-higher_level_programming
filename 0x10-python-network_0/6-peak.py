#!/usr/bin/python3
""" finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """ finds a peak in a list of unsorted integers """

    size = len(list_of_integers)
    if size == 0:
        return None
    if size == 1:
        return list_of_integers[0]
    if size == 2:
        return max(list_of_integers)

    mid = size//2

    peak = list_of_integers[mid]
    left = list_of_integers[mid - 1]
    right = list_of_integers[mid + 1]

    if peak > left and peak > right:
        return peak
    elif peak < left:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid:])
