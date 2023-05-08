[[COMP24112]]

### definition
- backpropagation is a method of calculating the ==gradient of the loss function== with respect to the layers of neural network weights
- essentially, by using backpropagation to find the gradient of the loss function with respect to a specific weight, you can then use that value with a technique like ==gradient descent== to update the weight, in the attempt of the neural network improving its predictions ([[gradient descent]])
- the ==chain rule== is used to iteratively compute the gradient of each layer
![](https://i.imgur.com/9ExTk2B.png)
- it can be seen as the process of calculating the error contribution of neurons in each layer after processing a batch of training data

### loss function + regularisation
- a loss function calculates error based on the weights provided, so is represented as $Loss(W_{NN})$, $NN$ being the neural network
- a ==regularisation term== can be added onto the final value in order to prevent ==overfitting== ([[overfitting and underfitting]])
- a similar idea is followed in [[regularised least squares]], where $\lambda \geq 0$ is a hyper-parameter
![](https://i.imgur.com/asPXla7.png)

### backpropagation explained
- $O(z,W_p)$ is the loss function, taking the new features and the ==weights from the prediction layer== (the last layer, beyond the hidden layers)
- $p$ stands for prediction
![](https://i.imgur.com/kiyo0a4.png)
