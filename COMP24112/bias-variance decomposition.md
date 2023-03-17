[[COMP24112]]

By doing 'mathematical calculations' (?), the expected squared error for a new test sample can be composed of the variance error + bias error

![](https://i.imgur.com/4VY0nXK.png)


- Bias error is how much the averaged prediction is close to the true value, hence $y - \hat{y}$. It's the same as shown above
- Variance error is how much the prediction varies among different realisations of the model - also the same as above, just with the $x$'s removed when shown on its own in the content
![](https://i.imgur.com/dcyfrlv.png)


- ==Over-fitting== is a result of low bias error, and high variance error, which may be the result of an over complex model that is too sensitive to small fluctuations in the training set
- ==Under-fitting== is a result of high bias error, but a low variance error, which may make sense for an excessively simple model