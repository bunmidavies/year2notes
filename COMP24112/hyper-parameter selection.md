[[COMP24112]]

- Different hyper-parameter settings correspond to different model options
![[Pasted image 20230214112630.png]]
- You basically need to use one of the [[data splitting methods]] to split into training and testing data first. Then based off this, you can again use another data splitting method to produce different models with their respective error estimates
- The box mentions that you may want to re-train the final model using all the training data - this is because if you've used another splitting method to test models 1 to $T$, then for any of these models you would have only used a subset of the entire training data to actually train it
![[Pasted image 20230214113241.png]]