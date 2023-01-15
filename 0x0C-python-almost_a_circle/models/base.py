#!/usr/bin/python3
"""first class Base"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns json string of dictionary list"""
        return json.dumps(list_dictionaries or [])

    @classmethod
    def save_to_file(cls, list_objs):
        """save to file"""
        try:
            save = cls.to_json_string([files.to_dictionary() for files in list_objs])
        except:
            save = "[]"

        with open(cls.__name__ + ".json", "w", encoding="utf-8") as me:
            return me
