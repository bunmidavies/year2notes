[[COMP24112]]

given limited data, you will probably encounter the following issues, which has been caused by the gap between the ==true error== and ==sample error==

- ==Bias== - not enough training samples, and the training sample error is not the same as the true error. So due to a model being trained by these samples, it will be ==optimistically biased== when providing estimates of the hypothesis over future unseen samples
- The typical way to deal with bias is by choosing a new set of test examples which are independent of the training examples

- ==Variance== - when providing a new set of test samples to combat bias, this new sample error can still vary from the true error. A smaller set of test samples can result in higher variance