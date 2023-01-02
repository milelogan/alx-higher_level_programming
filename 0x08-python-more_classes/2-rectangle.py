#!/usr/bin/python3

"""  a class Rectangle that defines a rectangle """


class Rectangle:
    """class rectangle"""

    def __init__(self, width=0, height=0):
        """a class method or instance"""
        self.width = width
        self.height = height

    def area(self):
        """area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """perimeter of a rectangle"""
        return 2 * (self.__width + self.__height)

    @property
    def width(self):
        """returns width"""
        return self.__width

    @property
    def height(self):
        """returns height"""
        return self.__height

    @width.setter
    def width(self, value):
        """gets the value of width"""
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

    @height.setter
    def height(self, value):
        """gets the value of height"""
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
