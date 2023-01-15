#!/usr/bin/python3
"""first class Base"""
import json
import os.path
import csv


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

        with open(cls.__name__ + ".json", "w", encoding="utf-8") as fn:
            fn.write(save)

    @staticmethod
    def from_json_string(json_string):
        """returns list of json string"""
        return json.loads(json_string or [])

    @classmethod
    def create(cls, **dictionary):
        """makes instance"""
        if cls.__name__ == "Rectangle":
            new_create = cls(1, 1)
        if cls.__name__ == "Square":
            new_create = cls(1)
        if new_create:
            new_create.update(**dictionary)
            return new_create

    @classmethod
    def load_from_file(cls):
        """load from file"""
        if not os.path.isfile(cls.__name__ + ".json"):
            return []
        else:
            with open(cls.__name__ + ".json", "r", encoding="utf-8") as fn:
                list_dict = cls.from_json_string(fn.read())
            return [cls.create(**dic) for dic in list_dict]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        try:
            save_file = [x.to_dictionary() for x in list_objs]
        except:
            save_file = '[]'
        keys = save_file[0].keys()
        with open(cls.__name__ + ".csv", "w") as fn:
            writer = csv.DictWriter(fn, keys)
            writer.writeheader()
            writer.writerows(save_file)

    @classmethod
    def load_from_file_csv(cls):
        if not os.path.isfile(cls.__name__ + ".csv"):
            return []
        else:
            with open(cls.__name__ + ".csv", "r") as f:
                reader = csv.DictReader(f)
                csvs = [row for row in reader]
                for row in csvs:
                    for key, val in row.items():
                        try:
                            row[key] = int(val)
                        except:
                            pass
            return [cls.create(**dic) for dic in csvs]
