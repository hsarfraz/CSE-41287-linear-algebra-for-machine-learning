## Terms

* normal line method
* gradient decent method

## weekly discussion
> The assignment README file instructions will guide you, there will be 3 plots generated. To get the full mark it is enough to submit the assignment table,  adding plots and your matlab scripts would be nice. The goal of the assignment is to inspire you to think how learning rate and number of iterations affect the final ML model. Using small practical example is easier to understand and  conceptually to generalize. Feel free to play with alpha and number of iterations. 
The learning rate "alpha" can be changed from default value 0.07 to bigger value, on example 0.1. How is changing learning rate "alpha" going to influence your linear regression model?

The learning rate alpha controls the size of the step the ML model takes to reach the weights (which would produce the least squared minimum error) in Gradient Descent. 

* If the learning rate (alpha) is **too small** then the ML algorithm will find the optimal weights very slowly. As a result, it would take many iterations to to reach the minimum cost function (the function that has the weights which would produce the least squared minimum error for the ML model)
* If the learning rate (alpha) is **too large** then the ML algorithm will not be able to find the optimal weights for the ML model. It would most probably go over the optimal weights since the step size (to go from one weight to another) would be really big. 

To find the optimal learning rate (alpha), you would need to find a middle ground where the learning rate (alpha) isn't too high or too low. That way, you will be able to get a learning rate which can give the best weights which would minimize the least squared minimum error of the ML model where is can give the most accurate results.
