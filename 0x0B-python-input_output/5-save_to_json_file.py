#!/usr/bin/python3
"""write to json file"""


def save_to_json_file(my_obj, filename):
    """funtion that writes an object file"""
    with open(filename, "w") as fname:
        return fname.write(json.dumps(my_obj))
