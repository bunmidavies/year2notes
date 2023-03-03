[[COMP24112]]

- different models will give you different ways to formulate $p(\textrm{class k}|x)$
- [[cross entropy loss]] based on class posterior is firstly covered
- ==logistic regression = linear classification trained with cross-entropy loss==

- similar to regression, the ==likelihood/ log likelihood== function can be maximised, again using an MLE (maximum likelihood estimator)

### assumptions about class label distribution
- binary classification = bernoulli distribution
![](https://i.imgur.com/BOlvwoh.png)

- multi-class classification = multinomial/categorical distribution
![](https://i.imgur.com/lj4CiU6.png)

### likelihood of an individual sample
- assume we have a training sample $(x_i,y_i)$ (feature = $x$, true value = $y$)
- we use the distributions we have assumed in the section above
![](https://i.imgur.com/EfTGJjy.png)


### likelihood of $N$ training samples
- we assume sample independence
![](https://i.imgur.com/snttlcB.png)


### negative log likelihood loss
- negative log likelihood for classification is equal to the [[cross entropy loss]], if:
	- $\theta(x) = p(c_1|x)$
	- $\theta_k(x) = p(c_k|x)$
