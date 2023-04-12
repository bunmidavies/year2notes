[[COMP24112]]

### ~ definition
A complete machine learning experiment includes:
- model training 
- model evaluation
- model selection: selecting a best model among different options (aka [[hyper-parameter selection]])

==Training, evaluation and hyper-parameter selection should not happen using the same sample set==

When splitting data, you should use the [[data splitting methods]] i.e. the different splitting methods like hold-out, random subsampling, K-fold cross validation, etc.