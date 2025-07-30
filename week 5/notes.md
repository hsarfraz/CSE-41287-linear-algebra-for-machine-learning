# Key Terms
<ins> Change of basis video </ins> [here is the link](https://www.youtube.com/watch?v=P2LTAUO1TdA) 
* scalars

# Quiz Terms
* eigenvectors
* eigenvalues
* matrix transformations (matrix stretch/compress the eigenvectors by different amounts)
* system of linear equations vs. eigenvectors
* ordered basis
* diagonalizable square matrix
* orthogonal vectors


# Discussion

**Question 1**: Matrix decompositions are workhorse in Machine Learning that powers applications like finding matrix inverse, least squares model fitting and reducing system dimensionality. One of the most used decompositions, QR matrix decomposition is a result of Gram-Schmidt algorithm in theory, but in reality is implemented using more stable algorithm. If you think of QR as a result of GS orthogonalization can you explain why is matrix R upper triangular?

Before I write a response to this question I am going to be addressing some questions that I had

<ins> What is the purpose of orthogonal matrices/what is their purpose? </ins>

A orthogonal matrix rotates or flips/reflects a vector and does not stretch or compress the vector. It preserves the length/norm and angle between vectors.

<ins> What is QR decomposition and what is it's purpose? </ins>

QR matrix decomposition (aka QR factorization) is a method of breaking a matrix down to smaller parts to make certain calculations easier (ex. such as solving for a system of linear equations - please note that reduced row echelon form (RREF) is **_different_** than QR matrix decomposition). The formula for QR decomposition is. 

A = Q * R

* Q: matrix with orthonormal columns
* R: upper triangular matrix. All entries below the diagonal are zero

<ins> What is the Gram-Schmidt algorithm and what is its purpose? </ins>

The Gram-Schmidt algorithm turns a set of linearly independent vectors to a orthonormal (note, different than orthogonal) set. Which means the vectors are orthogonal and normalized (each vector has a length of 1 when you calculate the distance from the vector point to origin)

<ins> Answer </ins>

QR matrix decomposition, when applied with Gram-Schmidt orthogonalization/algorithm, builds a orthogonal basis step-by-step. This means that each column is written as a linear combination of the previous vectors and itself. Each new vector only depends on the current and earlier vectors, when the entries below the diagonal in the matrix R are zero, then the output matrix is upper triangular.

**Question 2**: Transforming images plays a big role in Machine Learning and eigentheory and "change of basis"  are used in algorithms in image processing on pixel coordinates transformed into new coordinates. What is the difference between "similar" and "equivalent"  matrices of transformation?

<ins> What is a similar matrix? </ins>

* Are the same size
* Represent the same linear transformation but with different basis
* Share eigen values
* Used in change of basis (when you are expressing the same transformation under a new basis)

<ins> What is a equivalent matrix? </ins>

* Can be different sizes
* Represent the same linear transformation with the change of basis in the same domain and codomain
* Rank for both matrices are equivalent but not eigen values
* Used when comparing general linear maps

<ins> Answer </ins>

Similar matrices represent the same linear transformation under different basis in the same vector space. They change how you represent the transformation (like rotating or scaling an image), but the actual transformation stays the same.

Equivalent matrices represent linear transformations that are functionally the same in terms of input–output behavior (like same rank), but between different vector spaces or after changing both the input and output basis. 
