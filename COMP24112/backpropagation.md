[[COMP24112]]

- backpropagation is a method of calculating the gradient of the loss function with respect to the layers of neural network weights
- the ==chain rule== is used to iteratively compute the gradient of each layer
![](https://i.imgur.com/9ExTk2B.png)

- it can be seen as the process of calculating the error contribution of each neuron after processing a batch of training data

- the output of this process is the loss function, $O(z,W_p)$
- a ==regularisation term== can be added onto the final value in order to prevent ==overfitting== ([[overfitting and underfitting]])
- a similar idea is followed in [[regularised least squares]], where $\lambda \geq 0$ is a hyper-parameter
![](https://i.imgur.com/asPXla7.png)

- $W_{NN}$ is the sum of all the squared weights
![](https://i.imgur.com/kiyo0a4.png)
