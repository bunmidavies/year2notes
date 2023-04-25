[[COMP24112]]

### definition
- as shown previously within [[linear least squares]] / [[regularised least squares]], it is possible to turn the [[optimality condition]] of some parameters within a model into a set of linear equations (and then into normal equations and solve them)
- the problem is that loss functions can become more complex, making them no longer linear equations (i.e. ==nonlinear==)
- ==it is often impossible to solve a set of nonlinear equations==
- there are a number of iterative approaches which exist instead, intending to minimise the loss function:
	- [[gradient descent]]
	- [[stochastic gradient descent + mini-batch gradient descent]]

### links
- https://elitedatascience.com/machine-learning-iteration