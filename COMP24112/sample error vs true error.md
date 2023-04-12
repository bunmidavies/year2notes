[[COMP24112]]

### ~ sample error: definition
- hypothesis = a prediction made by an ML model
- the sample error of a hypothesis is written as $\textrm{error}_s$
- sample error = ==error computed using a set of data samples==

### ~ true error: definition
- for classification, true error is the ==probability that a single sample is misclassified==, where the sample is randomly drawn from a distribution
- for regression, it is the ==expectation of the error==
- the true error is actually what we wish to know at all times - but it can be very hard or even not possible to compute this
- calculating the true error can take the following steps:
	1. training the model using training data $T$
	2. ==estimating== the true error using new test data $E$
- its not possible to calculate the true error, so we now run multiple training-
- ==Infinite samples==: samples converge to a true error
- ==Insufficient samples==: sample error may not approximate to the true error well

### ~ sample error vs true error
![](https://i.imgur.com/vMd7iYC.png)
- ==We can always compute the sample error==
- meanwhile true error can be very difficult to compute, or in some cases not possible to compute at all


