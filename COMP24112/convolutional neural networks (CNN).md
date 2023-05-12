[[COMP24112]]

### definition
- a convolutional neural network is a type of ==artificial neural network==
- the main difference between a CNN and a traditional neural network is that CNNs use ==2D and 3D neurons== - the layers in the CNN have neurons which are arranged in 2 or 3 dimensions (the 3 dimensions being width, height and depth)
- as well as this, CNNs contain both ==convolutional layers== and ==pooling layers==
- the training of a CNN is based on [[backpropagation]] and ==stochastic gradient descent== ([[stochastic gradient descent + mini-batch gradient descent]])

### convolutional layers
- within convolutional layers, the idea of ==local connectivity== is introduced
- instead of a neuron being connected to every other neuron in the previous layer, its only connected to a small region of the previous layer
![](https://i.imgur.com/ce8ML9s.png)
- the output of the neuron is computed from the output of the previous layer, and the weights of a convolutional filter - $y = \textrm{Activation}(w^Tx+b)$
- this convolutional filter slides over all neurons in the layer - this is so that the same weights are used across all neurons
![|650](https://i.imgur.com/YhfJ1BQ.png)
- the ==stride number== determines how much you move the filter by - for instance a stride number of 1 will move the filter across all possible locations
- the resulting activation map size can be generalised with the following formula:
$$(\frac{N-F}{S}+1)\times(\frac{N-F}{S}+1)$$
- $N$ = input layer size
- $F$ = convolutional filter size
- $S$ = stride size
- the format is always ==width x height x depth== (so the first two equations above are width and height)

- this formula is slightly changed when dealing with 3D neurons and convolutional filter, but one activation map is still returned
![](https://i.imgur.com/T0IsLgB.png)
- typically, ==multiple convolutional filters are applied== - $T$ convolutional filters will result in $T$ separate activation maps
![|450](https://i.imgur.com/KglZ5It.png)

### pooling layer
- the pooling layer takes the activation maps returned from convolutional layers as input, then reduces the size of each activation map separately
- this process can be viewed as a sort of ==down-sampling== process
- a pooling filter slides over the activation map similar to how the convolutional filter does
- a common pooling filter is a ==max pooling filter== - which just takes the max value within each value currently in the filter
![](https://i.imgur.com/TWtjj4U.png)

### flattening 
- the output of a convolutional layer will typically be a set of activiation maps which can be stored in a 3D array
- these values can be ==flattened== to a 1D array - e.g. 32 x 32 x 5 array -> 5120 x 1 array
- this fully flattened layer is essentially a 1D neuron setup, which can be passed into a multilayer perceptron ([[artificial neural networks]])
- finally, some 1D output can be obtained from the multilayer perceptron

### final architecture of CNN
![](https://i.imgur.com/i5RMkCN.png)
