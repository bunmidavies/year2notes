[[COMP24112]]

## training, validation and testing
- within hyper-parameter selection, its important to split the data into 3 main sets for the following purposes:
	1. Training - a set of samples used for learning, to optimise model parameters
	2. Validation - a set of samples used to select (==tune==) the hyper-parameters
	3. Testing - a set of samples used ==only to assess the performance== of a fully-specified classifier (i.e. a classifier which has been trained with the selected/tuned hyperparameters)

- Different hyper-parameter settings correspond to different model options
![](https://i.imgur.com/ktYhgcY.png)

- You basically need to use one of the [[data splitting methods]] to split into training and testing data first. Then based off this, you can again use another data splitting method to produce different models with their respective error estimates
- The box mentions that you may want to re-train the final model using all the training data - this is because if you've used another splitting method to test models 1 to $T$, then for any of these models you would have only used a subset of the entire training data to actually train it
![](https://i.imgur.com/HgO8V0s.png)
