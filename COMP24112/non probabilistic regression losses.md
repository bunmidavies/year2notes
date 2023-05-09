[[COMP24112]]

- one of the most common loss functions for regression models is the ==RMSE==, i.e. root mean squared error 
- some regression losses are simplified versions of RMSE, using training samples

![](https://i.imgur.com/KhiKEbz.png)
- $\hat{y}$ = ==prediction for training sample==
- $y$ = ==correct answer for training sample==
- note that the half multiplication for sum-of-squares exists to make the derivative of the loss function easier to calculate later on

### example
![](https://i.imgur.com/YUsen75.png)

### linear least squares + regularised linear least squares

- ==linear least squares== = training a linear model by minimising the sum-of-squares error loss
- a regularisation term can then be added to this error function (<span style="color:red">term in red</span>)
![](https://i.imgur.com/gGITPVp.png)
- the benefit of regularisation is that it prevents the model from ==overfitting== to training data
- when $\lambda$ is too large, ==underfitting== will occur
- [[overfitting and underfitting]]
