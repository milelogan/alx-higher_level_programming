#!/usr/bin/python3
""" append to a file"""


def append_write(filename="", text=""):
    """appends to a file"""
    with open(filename, mode="a+", encoding="utf-8") as f:
        return f.write(text)
