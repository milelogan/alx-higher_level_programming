#!/usr/bin/python3
"""first class Base"""


class Base:
    """class package Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """class contributor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
