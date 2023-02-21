[[COMP24112]]

### classification by probabilistic inference

classification can be performed using a [[discriminant function]], but can also be performed in a probabilistic manner

- the ==posterior class probability== is modelled - $p(\textrm{class k}|x)$. This is the probability that given input $x$, the output is class $k$
- the ==most likely class== is the output of the function: $\hat{y} = \textrm{argmax} p(\textrm{class k}|x)$
![](https://i.imgur.com/0fzWlq8.png)

- in this example, since dog is the most likely class, it is the class which the function will return


### regression by probabilistic inference

- to perform regression by probabilistic inference, the ==posterior output probability== is modelled - $p(f|x)$
- the output is estimated by using the ==conditional mean== - $\hat{y} = E_f[f|x]$

### modelling the posterior class probability

- ==directly constructing the posterior== is one approach - [[logistic regression]] belongs to this approach
- the other approach covered involves constructing the ==likelihood== and ==prior==, then computing the posterior by using bayes theorem ([[Bayesian Updating]])
![](https://i.imgur.com/4fy7eZm.png)

![](https://i.imgur.com/2LOBMtF.png)

- in this image, there is the most likely output, but all outputs have a probability assigned to them in order to model $p(f|x)$ ?