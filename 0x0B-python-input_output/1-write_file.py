#!/usr/bin/python3
""" write a file"""


def write_file(filename="", text=""):
    """write a file that doesn't exist and overrite"""
    with open(filename, mode="w", encode="utf-8") as f:
        return f.write(text)
