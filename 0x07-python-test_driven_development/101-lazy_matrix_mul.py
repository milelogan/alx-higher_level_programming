#!/usr/bin/python3

""" a function that multiplies 2 matrices by using the module NumPy"""

import numpy as np

def lazy_matrix_mul(m_a, m_b):
	"""
	Using numpy module to multiply two matrices

	Args:
		m_a: first matix
		m_b: second matrix
	
	Returns:
		the value of multiplication of matrix
	"""

	return (np.matmul(m_a, m_b))

