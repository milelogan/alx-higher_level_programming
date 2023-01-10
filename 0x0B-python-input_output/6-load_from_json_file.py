#!/usr/bin/python3
""" load a json file"""

import json


def load_from_json_file(filename):
    """function that loads from a json file"""
    with open(filename, "r") as floc:
        return json.load(floc)
