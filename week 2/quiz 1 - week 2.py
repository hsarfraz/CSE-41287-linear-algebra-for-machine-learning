# -*- coding: utf-8 -*-
"""
Created on Sun Jul 13 12:35:58 2025

@author: hussainsarfraz
"""

### Question 1

from sympy import Matrix

A = Matrix([
    [2, -4, -1, 1],
    [1, -3, 1, 1],
    [3, -5, -3, 1]
])

# calculating determinant

A1 = Matrix([
    [2, -4, -1],
    [1, -3, 1],
    [3, -5, -3]
])

det_A = A1.det()

print("Determinant of A:", det_A) 
""" output
Determinant of A: 0
"""


# Use Gauss Jordan Elimination by reducing the matrix to reduced row echelon form
rref_matrix, pivot_columns = A.rref()

print("RREF:")
#print(rref_matrix)
for i in range(rref_matrix.rows):
    print(rref_matrix.row(i))
    
""" output
RREF:
Matrix([[1, 0, -7/2, -1/2]])
Matrix([[0, 1, -3/2, -1/2]])
Matrix([[0, 0, 0, 0]])
"""

### Question 2

## method 1: using sympy
u = Matrix([3,1,4])
v = Matrix([2,2,-4])

print(u.dot(v)) #output: -8

## method 2: using numpy
import numpy as np

# Define your vectors (as 1D arrays)
a = np.array([3,1,4])
b = np.array([2,2,-4])

# Compute the dot product
dot = np.dot(a, b)

print(dot) #output: -8

### Question 4
A = Matrix([
    [3, 1],
    [2, 1],
    ])

print(A**3) #output: Matrix([[41, 15], [30, 11]])


### Question 5
A = Matrix([
    [1, 2],
    [3, 4]
])

B = Matrix([
    [9, 8],
    [7, 6]
])

# Transpose
A_T = A.T
B_T = B.T

# Order matters in matrix multiplication because it isn't commutative
print(A_T * B_T) #output: Matrix([[33, 25], [50, 38]])
print(B_T * A_T) #output: Matrix([[23, 55], [20, 48]])
