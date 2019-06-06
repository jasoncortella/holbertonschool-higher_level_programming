c#!/usr/bin/python3

def add_attribute(obj, attribute, value):
    """Add an atribute to an object if it is possible"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
