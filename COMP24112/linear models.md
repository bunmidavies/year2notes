[[COMP24112]]

### ~ definition
- a linear model is the simplest type of ==parametric model== to exist in ML ([[parametric + non-parametric models]])
- linear models make use of a ==linear function== to construct a predicted output
- a linear function can either return a ==single output== or ==multiple outputs== ([[single-output functions + multi-output functions]])
- this linear function is essentially just a ==weighted sum==, where:
	- parameters = weights / coefficients
	- inputs get multiplied by weights

### ~ single output

a number of weights/coefficients are combined with the input variables, alongside a ==bias parameter==

$$\hat{y} = w_0 + w_1x_1 + ... + w_dx_d$$

and in order to get the matrix representation of the model, we introduce an expanded feature vector:
$$\tilde{x} = [1,x_1,...,x_d]$$

- using this matrix representation, ==each row represents a sample==
- the weights and output can then be put into vectors, where the $n$th row represents the output for the $n$th sample
- therefore $\hat{Y} = \hat{X}w$


### ~ multiple outputs

for a linear function with multiple outputs, we create different linear functions for every single output value, meaning our weights vector which was used for single output functions, becomes a matrix for multi-output functions
![](https://i.imgur.com/HXQkjYr.png)

- therefore the prediction for a single sample is:
$$\hat{y} = W^T\tilde{x}$$
- where $W^T$ is a singular vector extracted from the matrix for the according sample
![](https://i.imgur.com/UuFTovt.png)

### linear model for classification

- using this function which has been constructed, now the function can be used for [[classification]]
- a [[discriminant function]] can be applied to either the single output or multiple outputs - in the case of the multi-output functions, an input will then be considered to belong to multiple classes

### linear model for classification ==with probabilistic inference==

logistic regression involves using a linear model for classification combined with ==probabilistic inference==

it is possible to compute the ==class posterior== from a linear model, by using the logistic sigmoid or softmax function (depending on whether we are doing binary classification or multi-class classifcation)
- basically, for a single-output linear model, the logistic sigmoid function converts this real valued number into a probability
  ![](https://i.imgur.com/JNACPkB.png)

  - meanwhile for multi-class classification involving a multi-output linear function, we use the ==softmax== function in order to convert each of the outputs into separate probabilities
![](https://i.imgur.com/qsUrYss.png)

- example of the softmax function working:
![](https://i.imgur.com/7cyy6zb.png)

- logistic regression (which just uses the softmax function as shown above
![](https://i.imgur.com/SYaBBTE.png)


### linear model for regression
using a linear model for regression is focused on the case where a single-output function is used

- Non-probabilistic / deterministic approach - use the output as the predicted value
- Probabilistic approach - $p(f|x)$ is estimated using:
	- Gaussian distribution: $p(f|x) = N(W^T\tilde{x},\sigma^2)$
	- Adding Gaussian noise with zero mean and variance $\sigma^2$ to the output of a linear model:
	  $$\hat{y} = W^T\tilde{x} + \varepsilon$$