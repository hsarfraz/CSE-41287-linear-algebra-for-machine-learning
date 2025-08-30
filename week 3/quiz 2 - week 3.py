# -*- coding: utf-8 -*-
"""
Created on Sat Aug 30 04:03:16 2025

@author: hussainsarfraz
"""

from sympy import Matrix

# use gauss jordan elimination to transform matrix A to reduced row echalon form (RREF)

matrix_A = Matrix([
    [1,2,0,1],
    [1,2,1,2],
    [0,0,1,1]
    ])

matrix_B = Matrix([1,2,1])

solution = matrix_A.gauss_jordan_solve(matrix_B)

print(solution)

''' Output
(Matrix([
[-2*tau0 - tau1 + 1],
[              tau0], #free variable
[          1 - tau1],
[              tau1]]) #free variable
    
    , Matrix([
[tau0],
[tau1]]))
'''


# Use Gauss Jordan Elimination by reducing the matrix to reduced row echelon form
A = Matrix([
    [1,2,0,1,1],
    [1,2,1,2,2],
    [0,0,1,1,1]
    ])

rref_matrix, pivot_columns = A.rref()

print("RREF:")
#print(rref_matrix)
for i in range(rref_matrix.rows):
    print(rref_matrix.row(i))
    
'''Output
Matrix([[1, 2, 0, 1, 1]])
Matrix([[0, 0, 1, 1, 1]])
Matrix([[0, 0, 0, 0, 0]])
'''