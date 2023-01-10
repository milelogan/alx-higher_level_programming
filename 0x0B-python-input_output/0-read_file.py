#!/usr/bin/python3

"""REad file"""


def read_file(filename=""):
    """a function that reads file using with function"""
    with open(filename, mode="r", encoding="utf-8") as f:
        for p in f:
            print(p, end="")
