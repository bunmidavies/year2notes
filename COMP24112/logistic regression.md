[[COMP24112]]

### definition
- logistic regression despite the name, essentially uses a linear model with probabilistic inference to perform both ==binary classification== and ==multiclass classification==
- it is possible to compute the ==class posterior== from a linear model ([[linear models]]), by applying one of the two functions to the output of the linear model:
	- ==logistic sigmoid== - used for binary classification
  ![](https://i.imgur.com/JNACPkB.png)
	- ==softmax function== - used for multi-class classification, to create separate probabilities
![](https://i.imgur.com/qsUrYss.png)

- example of the softmax function working:
![](https://i.imgur.com/7cyy6zb.png)

- logistic regression (which just uses the softmax function as shown above
![](https://i.imgur.com/SYaBBTE.png)

