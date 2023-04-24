[[COMP24112]]

### parametric models
- a ==parametric model== is any model which captures all the information about its predictions with a ==fixed== set of parameters
- more importantly, parametric models make assumptions about ==the form of the mapping of inputs -> outputs==
- the most common example of a parametric model is something like ==linear regression== - the model essentially assumes that inputs -> outputs can be mapped with some kind of straight line
- parametric models are typically simpler / faster than non-parametric models

### non-parametric models
- a ==non-parametric model==, contrary to a parametric model, will make no assumption (or no strong assumption) about the form of the mapping from inputs to outputs
- this means non-parametric models ==can take on any functional form from training data==
- the most common example of a parametric model the is [[k nearest neighbour (k-NN)]] model - no actual assumption is made about the functional form of the training data provided, the model just assumes that close patterns = similar output
- non-parametric models are typically more flexible than parametric models, but are ==slower== and require more training data