[[COMP24112]]

`chapter 1`

- The basic understanding of what machine learning is, brief history of ML and when it started
- Why machine learning is important, and what applications it has today

- All machine learning systems are compromised of: data, a mathematical function, objective/loss function, training algorithm
- creating a machine learning model / the ml pipeline

- Supervised learning: "teacher" providing expected outputs
- Unsupervised learning: no "teacher"
- Reinforcement learning: reward/punishment
- classification, and the different types of classification
- regression

`chapter 2`

- k-NN is the simplest ML algorithm, building on the idea of instance based learning
- k-NN can be used for both classification and regression
- k-NN involves no explicit training, and relies on distance measure
- more training data = more info to learn + more accuracy, but higher memory / time consumption
- k is a user chosen parameter (a hyper-parameter)
- too small k - sensitivity to noise in samples
- too large k - inaccuracies in prediction

...

`chapter 6`

- there are different approaches for minimising a loss function - some involve you solving linear systems (i.e. zero gradient), while others are iterative (e.g. gradient descent)
- the aim of linear least squares method and regularised linear least squares method is to minimise the loss function for a given model - the minimisation of the loss function takes place within the training phase in the machine learning pipeline

...

`chapter 8`