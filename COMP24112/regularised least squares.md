[[COMP24112]]

### definition
- ==regularisation== has been mentioned before within ML, and exists basically to avoid ==overfitting== ([[overfitting and underfitting]])
- the same idea within [[linear least squares]] then follows, where you set the gradient function to zero, and try to solve this in order to find the parameters which satisfy the [[optimality condition]]
- the only difference here is that you have a ==regularisation term added on== - $\frac{\lambda}{2}w^Tw$
![ | 550](https://i.imgur.com/eUiiZl0.png)
- note that $\lambda > 0$ is a ==hyper-parameter== and, therefore must be selected - it controls the ==balance== between the data dependent error function and the regularisation term
- ==steps for loss function -> optimal weight vector==:
	1. $minO_\lambda(w)$ is the loss function + regularisation term
	2. ==differentiate== $\textrm{minO}_\lambda(w)$ with respect to $w$
	3. this derivative is then set to 0, and solved for $w$

### applications
- travel time prediction: predicting the ==travel time== for a future journey on a certain 'road segment' (journey), given 15 measurements collected for the same road segment
![ | 550](https://i.imgur.com/a5DjSH6.png)
- iris classification: given measured sepal lengths and petal widths of 150 iris samples, classify irises as one of two types: versicolour or virginica
![ | 550](https://i.imgur.com/JESgmX9.png)
- non linear regression: construction a curve that has the best fit to a series of data points - the method to do this involves incorporating ==basis functions== ([[handling non-linear data patterns]]) to a [[linear least squares]] model
![ | 550](https://i.imgur.com/e9z9iZR.png)
- iris classification again, but using the regularised least squares approach, and selecting the hyperparameter $\lambda$
![ | 550](https://i.imgur.com/RQhbpr1.png)
