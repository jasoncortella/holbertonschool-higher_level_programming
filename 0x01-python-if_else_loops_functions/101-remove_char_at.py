#!/usr/bin/python3
def remove_char_at(str, n):
    return str[:n] + str[n+1:] if n >= 0 else str
