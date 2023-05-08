[[COMP24112]]

### intro + background
- an artificial neural network is a computing system that is ==inspired by==, but not identical to, biological neural networks that constitute animal brains
- artificial neural networks were initially proposed in the hope that they could solve problems in the same way a human does - however, over time the attention has shifted to performing ==specific tasks==, thus deviating them from biology
- the first computational model for a neural network was created in ==1943== by Warren McCulloch and Walter Pitts - in ==1957==, the perceptron algorithm was invented, and around the 60s-80s concepts like convolutional neural networks and recurrent neural networks became popularised

### neuron structure
- artificial neural network = collection of ==artifical neurons==, connected together
- each artificial neuron simulates a real neuron - ==multiple inputs -> 1 output==
- the multiple inputs are received from other neurons - connection strengths determine how the signals are accumulated, and the neuron fires a signal if enough signals accumulate
- singular neurons are similar to multi-input single output [[linear models]], with an ==activation function== added on top
![](https://i.imgur.com/SDztApk.png)
- the linear model weights $w$ control the strength of the incoming signals, and the resultant sum is used as an input for the ==activation function==

### activation functions
- the activation function is applied to the weighted sum returned by the ==adder== in the neuron
- there are a number of standard activation functions which can be used - for instance, the identity function simply returns the resultant sum from the neuron's adder
![](https://i.imgur.com/JZRl8wT.png)


### single layer perceptron
- a single layer perceptron has one input layer, and one output layer - similar to multi-input multi-output [[linear models]]
- both layers are just groups of neurons
![](https://i.imgur.com/l9J8H0w.png)


### multilayer perceptron
- a multilayer perceptron aka a ==feedforward artificial neural network==, consists of ==at least 3== layers of nodes - input, at least one hidden, and output
- currently, the single layer perceptron has 2 layers, one of which for input and the other for output, resembling a linear model
- by adding hidden layers, ==nonlinear, more complex functions can be formulated==
- each of the hidden layers find a ==partial solution==, and is combined in the next layer
![](https://i.imgur.com/vYQySyv.png)
![](https://i.imgur.com/cPl3EBa.png)


### 1 hidden layer example - XOR
- consider the XOR problem as a classification problem - there is no singular line which can correctly separate an output of 1 from an output of 1, given the following points
![](https://i.imgur.com/81lOrJL.png)

- so by essentially creating singular lines, and combining them to form an entire solution, you've solved the problem using multiple layers
![](https://i.imgur.com/siriS9h.png)


### multilayer perceptron mapping example
![](https://i.imgur.com/frl83Wp.png)


### multilayer perceptron application - handwritten digits
- each image of a handwritten digit has dimensions of 28x28, thus can be represented with a vector of length 784 (28x28)
![](https://i.imgur.com/hcBv3rC.png)
