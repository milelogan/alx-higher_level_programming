#!/usr/bin/python3
""" square.py"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class square inheriting square"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """gets the size"""
        return self.width

    @size.setter
    def size(self, value):
        """sets size"""
        self.width = value
        self.height = value

    def __str__(self):
        """prints strings"""
        return "[{}], ({}), {}/{} - {}".format(
            type(self).__name__, self.id, self.x, self.y, self.size
        )

    def update(self, *args, **kwargs):
        """updates the square"""
        if args:
            i = 0
            keys = ["id", "size", "x", "y"]
            for arg in args:
                setattr(self, keys[i], arg)
                i += 1
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        sq_dict = {"size": self.width, "id": self.id, "x": self.x, "y": self.y}
        return sq_dict
