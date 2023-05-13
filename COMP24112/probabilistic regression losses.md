[[COMP24112]]

### definition
- instead of maximising/minimising a loss function in a non probabilistic manner ([[non probabilistic regression losses]]), a model can be trained by maximising the ==likelihood== (or log likelihood) function of the training samples
- ==likelihood==: given the observed data, likelihood is the probability of the observed data given the current model parameters
- ==log likelihood== is just the natural log of the likelihood
- a function called a ==maximum likelihood estimator (MLE)== is used in this case

![](https://i.imgur.com/iNXa9SP.png)
- the log of $L$ overall is equivalent to the sum of the individual logs of the likelihoods

### MLE for linear regression example
- the likelihood of $N$ training samples can be calculated (assuming a gaussian distribution for likelihood estimation)
- in this example MLE is essentially equivalent to the sum-of-squares error minimisation
![](https://i.imgur.com/z9Z4EkC.png)
- the log likelihood can then be calculated, using 2 constants and then the sum-of-squares error function ([[non probabilistic regression losses]])
![](https://i.imgur.com/C74op5d.png)
