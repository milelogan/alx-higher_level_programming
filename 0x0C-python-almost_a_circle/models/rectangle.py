#!/usr/bin/python3
""" class rectangle"""

from models.base import Base


class Rectangle(Base):
    """class rectangle that inherits class base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def error_checker(self, name, value):
        """checks or validates for errors"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if (name == "width" or name == "height") and value <= 0:
            raise ValueError(f"{name} must be > 0")
        if (name == "x" or name == "y") and value < 0:
            raise ValueError(f"{name} must be >= 0")

    def __str__(self):
        """prints string"""
        return "[{}] ({}) {}/{} - {}/{}".format(
            type(self).__name__,
            self.id,
            self.x,
            self.y,
            self.width,
            self.height,
        )

    def update(self, *args, **kwargs):
        """updates the attributes by assigning keys"""
        if args:
            i = 0
            keys = ["id", "width", "height", "x", "y"]
            for n in args:
                setattr(self, keys[i], n)
                i += 1
        elif kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns a dict representation of Rectangle"""
        dictionary = {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }
        return dictionary

    @property
    def width(self):
        """returns width"""
        return self.__width

    @property
    def height(self):
        """returns height"""
        return self.__height

    @property
    def x(self):
        """returns x"""
        return self.__x

    @property
    def y(self):
        """returns y"""
        return self.__y

    @width.setter
    def width(self, value):
        """assigns value to width"""
        self.error_checker("width", value)
        self.__width = value

    @height.setter
    def height(self, value):
        """assigns value to height"""
        self.error_checker("height", value)
        self.__height = value

    @x.setter
    def x(self, value):
        """assigns value to x"""
        self.error_checker("x", value)
        self.__x = value

    @y.setter
    def y(self, value):
        """assigns value to y"""
        self.error_checker("y", value)
        self.__y = value

    def area(self):
        return self.width * self.height

    def display(self):
        """using for loop"""
        print("\n" * self.y, end="")
        print(
            "".join("" * self.x + "#" * self.width + "\n" for x in range(self.height)),
            end="",
        )
