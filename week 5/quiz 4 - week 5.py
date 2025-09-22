# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 23:14:38 2025

@author: hussainsarfraz
"""

import numpy as np

# calculating the eigenvalues of a matrix + squaring a matrix (Q1)

a = np.array([
    [-1,3],
    [2,0]
    ])

a_squared = np.dot(a,a)

print('Eigenvalues of matrix a: ', np.linalg.eigvals(a),
      '\nEigenvalues of matrix a squared: ', np.linalg.eigvals(a_squared))
print('---')

# calculating the inverse of a matrix + eigenvalues (Q2)

b = np.array([
    [0,2],
    [2,3]
    ])

b_inverse = np.linalg.inv(b)

print('Eigenvalues of matrix a: ', np.linalg.eigvals(b),
      '\nEigenvalues of matrix a squared: ', np.linalg.eigvals(b_inverse))
