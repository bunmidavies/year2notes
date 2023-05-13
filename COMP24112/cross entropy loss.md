[[COMP24112]]

### definition
- cross entropy measures the ==distance between probability distributions==
- its discrete version can be used to examine the distance between a predicted class probability and the true probability (i.e. the ==posterior== against the ==true probability==)
- we use the discrete version because we are calculating the probabilities of ==classes==, rather than continuous values

### cross entropy loss for binary classification
- $H(p,q) = -[p(1)log(q(1)) + p(0)log(q(0))]$
	- $p$ = true probability
	- $q$ = posterior
- 0/1 label coding is used for a sample $(x,y)$
- if $y=1$ then $x$ is from class 1, meaning $p(1)=100\%$ and $p(0)=0\%$
- if $y=0$ then $x$ is from class 0 meaning $p(1)=0\%$ and $p(0)=100\%$
- therefore $p(1)=y$ and $p(0)=1-y$

- cross entropy loss can then be calculated over $N$ training samples as such:
![](https://i.imgur.com/u9stmAS.png)


### cross entropy loss for multi-class classification
- $y_{ik} = 1$ means that the $i$th sample belongs to class $k$
- $y_{ik}=0$ means that the $i$th sample does not belong to class $k$
- cross entropy loss computed over $N$ training samples for multi-class classification is as such
![](https://i.imgur.com/MO632dQ.png)


### cross-entropy loss examples

![](https://i.imgur.com/bmLkBsC.png)
![](https://i.imgur.com/vWZcXIG.png)
