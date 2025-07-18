# Week 3 Terms

* Gauss Jordan Elimination
* Using elementary row operations (ERO) in Gauss Jordan Elimination
* Augmented matrix
* Pivots
* Under determined Matrix System of Linear Equations
* Over determined Matrix System of Linear Equations
* Dependent Variables
* Free Variables
* Homogeneous system of linear equations
* Non-homogeneous system of linear equations
* Rank of a matrix after Gauss Jordan Elimination
* Trivial solutions of a system of linear equations
* Non-trivial solutions of a system of linear equations
* Moore Penrose Pseudo Inverse

# Week 3 Discussion

> Neural Network demo is about modeling neural networks by solving system of linear equations. We consider first the scenario in which the input data features and output measurements produce a square system. If the input data/features and the output measurements are inconsistent, there is no set of weights that perfectly fits the data. In practical scenarios we have many data points, (often more than model parameters), and affected by noise they do not form a consistent set of linear equations. What method can we use in these scenarios?

Question: In practical scenarios we have many data points, (often more than model parameters), and affected by noise they do not form a consistent set of linear equations. What method can we use in these scenarios?

I believe the question is referring to the scenario where our input data matrix is not a square matrix but a non-square matrix (it is either a under or over determined system of linear equations). And it is the noise which creates the under-determined matrix (or over-determined matrix).

In this situation I believe you would need to find the Moore-Penrose Pseudo inverse of the non-square matrix (as shown in the week 3 demo on neural networks the matrix is created by the inputs to a neuron). The moore-Penrose pseudo inverse would then find the outputs/predicted values that minimizes the squared error between the actual and predicted points. 

As mentioned in lecture 4:

* underdetermined system = wide matrix (more columns than rows which means n>m)
* overdetermined system = tall matrix (more rows than columns which means n<m)

For a example of a under-determined system, I believe the system of linear equations example shared in lecture 2 is a perfect example. 

<ins> Response to Comments </ins>

> To the extent that I understand this question, one can use linear regression techniques that calculate a line such that the squared error between the model equation and the data points is minimized.  There are also techniques called 'Ridge Regression', 'least absolute shrinkage and selection operator (LASSO)', 'elastic net' and 'principal component analysis'.  I can only assume that we will be exposed to some of these techniques in this coarse.

I really liked how you brought up the point of linear regression techniques and how they can be used to find the least-squared error between the actual and predicted points. When I was writing my response I didn't think about how regression can be used to minimize the squared error.

I do wonder if it would be correct to say that the Moore-Penrose Pseudo inverse of non-square matrices are used when solving for linear regressions of a system.

> If there isn't a consistent set of linear equations (as is common with noisy data or overdetermined systems), we cannot find an exact solution. Instead, we aim to find a best approximate solution—specifically, the **least squares solution**, which minimizes the sum of squared errors: $||Ax - b||^2$
> 
> From the lectures, I learned that using the **Moore-Penrose Pseudoinverse** ($A^+$) is a powerful and general method to obtain this optimal solution. It works for every matrix regardless of its shape or rank, allowing us to effectively find a solution even when the traditional inverse ($A^{-1}$) does not exist.
> 
> While a pseudoinverse cannot transform a reduced-rank matrix into an identity matrix, it produces a matrix that is *"close"* to it in effect—returning a solution that best approximates the behavior of a true inverse.

