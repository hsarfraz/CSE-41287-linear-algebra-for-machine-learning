## matrix, vector, scalar
* A matrix is a 2D array with multiple rows and columns
* A vector is a 1D array. It can be _**thought of**_ as a matrix with only one row or one column. But there is no concept of rows and columns in this shape.
* A scalar is just a single number — no rows, no columns. A scaler can be used to scale a vector or matrix (e.g., multiply every element by 2)

## dot product
* The dot product is similar to matrix multiplication but not the same thing since the dot product is when two vectors are being multiplied. It is important to note that vectors are 1D arrays, but can also be 2D arrays if they are a column vector.

## The Determinant ([Illustration of determinant](https://www.youtube.com/watch?v=Ip3X9LOh2dk&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab&index=8))
* When the derterminant of a matrix is zero that means the matrix does not have a inverse
* When the determinant of the coefficient matrix is zero, it means that the system of linear equations does not have a unique solution, because the equations are not linearly independent. In this case, the system of linear equations could have:
    * Infinitely many solutions (if the system is consistent), or
    * No solution at all (if the system is inconsistent)
 
  ## Week 2 Discussion post

> We will discuss this week the "dot-product" demo. Neural networks are "trained" and values for the weights W are determined based on training data X. Initially the values are random numbers. Deep neural networks have multiple layers of neurons. If a weight is zero that neuron does not contribute to the next layer. For a single neuron where W & X are both vectors output Y was represented as y=w'*x instead of y=x'*w. Does it really matter ? 

> With two neurons, X is a matrix and the form was Y=X*W, why is that? 
