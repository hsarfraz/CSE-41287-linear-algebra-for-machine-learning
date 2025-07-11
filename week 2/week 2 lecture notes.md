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

If a neural network layer only has one neuron then the order in which the input vector and neuron weight is being multiplies does not matter. I say this because both, the input vector and neuron weight, are vectors and their output shape is the same, which is a 1 by 1 scaler.

The 1 by 1 scalar will be the y output if you were to multiply the transpose of the weights (w') with the vector x or the transpose of x (x') with the weights (w). I have illustrated this idea below with a example vector and a weight which belongs to a neuron.

> With two neurons, X is a matrix and the form was Y=X*W, why is that?

When a layer has two neurons then there are going to be two vectors which represent the weights. In this situation the order does matter since if you were to switch up the order of the input vector and the weights the resulting y output can be a different shape. I have included a screenshot below where I go through some example values of a neural network layer with two neurons.

<ins> Response to comments </ins>

> The order matters here because matrix multiplication is not commutative. When you multiple the rows to columns, you will be pairing different numbers together if you change the order. Unless, X and W are the same or if X and Y is a diagonal matrix with zeros on the non-diagonal.

Thank you for your illustrations for the multiplication of the vectors X and W. It helps put things in perspective.

I do have a question about your answer to question 2. You mention how if X and W are the same then matrix multiplication does become communicative. I don't think this is the case since wouldn't the order of the numbers change if we were to multiply X*W as W*X? (since both variables don't represent vector?

The point you mentioned about how matrix multiplication becomes communicative if you have two diagonal matrices, which have zeros on the non-diagonal, is a interesting point.
