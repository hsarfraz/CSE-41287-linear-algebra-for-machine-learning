# Singular Value Decomposition (SVD) [link to video](https://www.youtube.com/watch?v=gXbThCXjZFM)

* SVD helps reduces the dimensions of data that has many dimensions
* Fourier transform (FFT)
* Principle Component Analysis (PCA)
* Correlation

# terms used in quiz

# discussion board prompt

> For many SVD is the most important matrix decomposition in linear algebra, because it reveals the detailed inner information about the matrix. You have learned that for a symmetric matrix the singular values and the eigenvalues are the same. How about the singular vectors and the eigenvectors ?

If matrix A is symmetric then their singular vectors and eigenvectors will be the same. I have included the notes and question I wrote down when answering this question.

If matrix A is symmetric then:
* eigenvectors = singular vectors
* eigenvalues = singular values

If matrix A is not symmetric then:
* the eigenvalues of A are not equal to the singular values of A
* When you compute $A^T A$ or $A A^T$ (which produces a symmetric matrix) then the singular values of A are the square root of the eigenvalues ($\sigma_i = \sqrt{\lambda_i}$) of $A^T A$ or $A A^T$

<ins>**What is a symmetric matrix?**</ins>

A symmetric matrix is one that is equal to its transpose ( $A=A^T$ )

Here are some properties of a symmetric matrix:

1. All their eigenvalues will be real numbers (not complex numbers)
2. Their eigenvectors are always orthogonal or can be made orthogonal. Orthogonal eigenvectors of a matrix are eigenvectors that happen to be orthogonal to each other (in other words, the eigenvectors are at a 90 degrees angle to each other)
3. They are always diagonalizable ($A = Q \Lambda Q^T$). Q is the matrix of orthogonal vectors.

<ins>**What are singular values? How are they related with eigenvalues?**</ins>

Singular values are the diagonal entries of the matrix $\Sigma$ in the SVD formula. They are the square root of the eigenvalues in the matrix $A^T A$ or $A A^T$ (note, this is only applicable when A is a non-symmetric matrix)

Remember, eigenvalues tell us how a matrix can transform (stretch or shrink) its own eigenvectors without changing the direction of the eigenvector. Eigenvalues can only exist with square matrices.

On the other hand, singular values tell you how much the matrix stretches space along orthogonal directions, even if the matrix does not rotate or distort vectors. Unlike eigenvalues, singular values always exist. 

<ins>**Purpose of a symmetric matrix and singular values**</ins>

Symmetric matrices and singular values are used in singular value decompositions (SVD)

$$
A = U \Sigma V^T 
$$

* $U =$ left singular vectors (from $A A^T$. This matrix gives eigenvectors which form $U$)
* $\Sigma =$ diagonal matrix of singular values
* $V =$ right singular vectors (from $A^T A$. This matrix gives eigenvectors which form $V$)

> Is it more accurate to say that for a symmetric matrix, the absolute values of the eigenvalues and the singular values are always the same?

This is a valid question that you have raised which is something that I forgot to mention in my reply. There are situations when eigenvectors for a symmetric matrix can be negative so in these situations the absolute value of these negative eigenvectors would be equal to the singular values since singular values are always positive.
