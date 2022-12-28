#!/usr/bin/python3

""" a function that prints a square with the character # """

def print_square(size):
	"""
	Write a function that prints a square with the character #

	Args:
		size: it's the size length of the square
	
	Returns:
		TypeError: size must be an integer
		size must be >= 0
	"""

	if not isinstance(size, int):
		raise TypeError("size must be an integer")
	if size < 0:
	 	raise ValueError("size must be >= 0")
	if (isinstance(size, float) and size < 0):
		raise TypeError("size must be an integer")
	for i in range(0, size):
		for j in range(size):
			print("#", end="")
		print("")
