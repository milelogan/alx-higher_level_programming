#!/usr/bin/python3

"""  a class Rectangle that defines a rectangle """


class Rectangle:
    """class rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """a class method or instance"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        return("\n".join("{}".format(self.print_symbol) * self.width for x in range(self.height)))

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def area(self):
        """area of a rectangle"""
        return self.width * self.height

    def perimeter(self):
        """perimeter of a rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

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
