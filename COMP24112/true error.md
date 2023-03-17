[[COMP24112]]

like [[sample error]], true error involves a hypothesis - a prediction which has been made by a trained machine learning model. It has different cases for classification and regression

- For classification, true error is the ==probability that a single sample is misclassified==, where the sample is randomly drawn from a distribution
- For regression, it is the ==expectation of the error==

![](https://i.imgur.com/vMd7iYC.png)


the true error is actually what we wish to know at all times - but it can be very hard or even not possible to compute this

Hypothesis evaluation for the true error involves:
- training the model using training data $T$
- ==estimating== the true error using new test data $E$
- its not possible to calculate the true error, so we now run multiple training-testing trials, and average these test error rates (at this point [[data splitting methods]] can be used)