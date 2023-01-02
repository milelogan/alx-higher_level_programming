#!/usr/bin/python3

""" a class Rectangle that defines a rectangle """

class Rectangle:
	""" a class rectangle """
	
	def __init__(self, width = 0, height = 0):
		""" class method or instance defined first"""
		self.width = width
		self.height = height
	
	@property
	def width(self):
		""" property of width returning itself"""
		return self.__width
	
	@width.setter
	def width(self, value):
		""" Function of property setter that returns values"""
		self.__width = value
		if not isinstance(value, int):
			raise TypeError("width must be an integer")
		elif value < 0:
			raise ValueError("width must be >= 0")
	
	@property
	def height(self):
		"""Function of height that returns itself"""
		return self.__height
	
	@height.setter
	def height(self, value):
		""" function of setter that returns value"""
		self.__height = value
		if not isinstance(value, int):
			raise TypeError("height must be an integer")
		elif value < 0:
			raise ValueError("height must be >= 0")
