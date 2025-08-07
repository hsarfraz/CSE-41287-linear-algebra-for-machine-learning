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
* When you compute $A^T*A$ or $A*A^T$ (which produces a symmetric matrix) then the singular values of A are the square root of the eigenvalues ($\sigma_i = \sqrt{\lambda_i}$
) of  
 or 
.
