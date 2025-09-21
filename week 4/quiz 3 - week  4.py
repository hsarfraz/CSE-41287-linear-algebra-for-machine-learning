# -*- coding: utf-8 -*-
"""
Created on Sat Sep 20 23:07:12 2025

@author: hussainsarfraz
"""

from sympy import Matrix
import numpy as np
import sys
sys.tracebacklimit = 0

# multiplying a matrix and vector (Q2)

t = Matrix([
    [1,2,1],
    [3,6,4]
    ])

u = Matrix([-3,1,1])

v = Matrix([-2,1,0])

print(t*u)
print(t*v) #v is in the null space since the output is in a zero vector
print('---')

# reducing a matrix to reduced row echalon form (RREF) to see if a vector is in the span of the matrix (Q3)

a = Matrix([
    [2,3,-1],
    [1,-1,0],
    [0,5,2],
    [3,2,1]
    ])

b = Matrix([2,3,-7,3])
c = Matrix([0,0,0,0])
d = Matrix([1,1,1,1])

try:
    print(a.gauss_jordan_solve(b))
    print(a.gauss_jordan_solve(c))
    print(a.gauss_jordan_solve(d)) # no solution
except Exception as error_message:
    print(error_message)
print('---')

# dot product of two vectors (Q4)

e = np.array([-2,3,1,4])
f = np.array([1,2,0,-1])

print(np.dot(e,f))