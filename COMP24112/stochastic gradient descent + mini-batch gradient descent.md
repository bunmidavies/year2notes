[[COMP24112]]

- while [[gradient descent]] computes the gradient of the error function using ==all training samples==, stochastic gradient descent estimates the gradient of the error function using only ==one training sample==
- mini-batch gradient descent is a similar idea, but instead of just one sample, a ==small set of training samples== is used
![ | 750](https://i.imgur.com/sBvJIKr.png)

### gradient descent vs stochastic gradient descent
- the following shows how the two approaches iterate towards a minimum loss function, for an iris classification model
![ | 550](https://i.imgur.com/dqcEeRp.png)
