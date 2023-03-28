[[COMP24112]]

-  training [[artificial neural networks]] is the process of finding ==optimal neural network weights==

### hebbian learning rule
- the hebbian learning rule is inspired by Donald Hebbs biological discovery in 1949. The rules have been reformulated from the discovery's original description as:
	- if neurons on either side of a synapse are activated ==simultaneously==, the strength of that synapse should be selectively ==increased==
	- if neurons on either side of a synapse are activated ==asynchronously==, the strength of the synapse should be ==weakened or eliminated==
- ==a synapse is a connection between two neurons==

- ==original discovery description==: *"When an axon of cell A is near enough to excite cell B and repeatedly or persistently takes part in firing it, some growth process or metabolic change takes place in one or both cells such that A's efficiency, as one of the cells firing B, is increased"*

- we can model this mathematically:
	- the weight of two neurons $i$ and $j$ = $w_{ij}$
	- the output of the two neurons = $x_i$ and $z_j$
	- with each iteration, $w_{ij} = w_{ij} + \Delta w_{ij}$, where $\Delta w_{ij} = \eta x_i z_j$ 

### gradient based training
- gradient based training is the most common approach to neural network training
- the output features from a multilayer perceptron are used as the input of a ==linear predictor==
- a ==loss function== is then used to assess whether these outputs are good or not
- the aim is to then find the network weights which minimise this loss function - this is now an optimisation problem which can be solved with methods like [[stochastic gradient descent + mini-batch gradient descent]]
- in practice, gradient based training is more accurate and stable than hebbian learning