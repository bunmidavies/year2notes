[[COMP24112]]

### definition
- Wiki definition: *"The machine learning task of learning a function that maps an input to an output based on example input-output pairs"*
- the ==based on example input-output pairs== is basically what distinguishes supervised learning from [[unsupervised learning]]
	- A ==teacher== provides the expected output for each data pattern/input
	- These pairs of input to expected output are called ==pairs==
	- Supervised learning tasks include [[classification]] and [[regression]], the two of which differ based on their output type
- examples of supervised learning applications include:
	- Speech recognition
	- Facial recognition
	- Object recognition

### pros and cons: k-NN
- ==pros==:
	- [[k nearest neighbour (k-NN)]] is a simple intuitive method, which requires no training
	- k-NN can be used for both classification and regression, and can handle both linear/nonlinear patterns
	- k-NN is also easy to implement for multiclass classification
	- the main two decisions involving k-NN are also easy to make:
		- what hyperparameter value of $k$ should be used?
		- what distance measure should be used? ([[distance measuring for k-NN]])
- ==cons==:
	- k-NN is slow with large scale data - this is typically due to the computational complexity of distance calculation, and neighbour searching
	- since all training data must be stored, there is a high memory cost
	- k-NN isn't good at dealing with imbalanced data, as it is sensitive to outliers - k-NN will also typically be biased towards majority classes, which is why biased decisions may be made if data is imbalanced

### pros and cons: regularised LLS
- ==pros==:
	- [[regularised least squares]]/[[linear least squares]] is the most widely used modelling method - its what most people mean when they say they've used 'regression', 'linear regression', or 'least squares' to fit a model to specific data
	- can be used for both regression and classification
	- good use of the data is made - good results can be obtained with a relatively small amount of data
	- the model is easy to explain and understand
	- the model is also efficient - training/predicition is fast, and a low amount of memory is required
	- in linear least squares, no hyperparameter needs to be set - in the regularised case, there are two main things to decide:
		- the form of the ==regularisation term== ($L_2$, $L_1$)
		- the regularisation parameter
- ==cons==:
	- limited model expressive power - (regularised) linear least squares cannot deal with nonlinear data patterns
	- sensitive to outliers - when being used in classification, the performance can be sensitive to how the target output is set, and probabilistic interpretation is not offered

### pros and cons: logistic regression
- ==pros==:
	- [[logistic regression]] is a simple and effective method, typically for classification
	- training/prediction is fast, and a low amount of memory is required
	- no specific distribution is assumed within the model, and no hyperparameters must be set
- ==cons==:
	- logistic regression is typically used as a linear classifier - it cannot handle nonlinear data patterns
	- logistic regression isn't great for ==multi-class classification== - typically only suited to binary classification

### pros and cons: artificial neural networks
- ==pros==:
	- [[artificial neural networks]] are capable or learning and modelling nonlinear/complex relationships
	- neural networks are also able to generalise, supported by advanced training strategies
	- no restrictions and assumptions are applied to the input
	- all learned information is stored within network weights - artificial neural networks are a good choice for [[black box modelling]]
- ==cons==:
	- a good ==network architecture== must be determined - doing this is sometimes not straightforward
	- the training process can take a long amount of time for large data
	- it can be difficult to interpret the learned model (hence the black box appeal)
	- the solution from an ANN is a ==local optimal==

### pros and cons: support vector machines (SVMs)
- ==pros==:
	- [[support vector machines (SVMs)]] typically provide good performance, while being able to generalise, handling complex datasets and capturing intricate relationships
	- unlike ANNs, SVMs are not solved for local optima
	- SVMs are effective in high dimensional feature spaces (i.e. where the number of features is greater than the number of samples)
- ==cons==:
	- selecting a good kernel function as well as hyperparameters isn't easy
	- computationally intensitive like ANNs - training time is long for large scale data
	- similar to ANNs, it can also be difficult to interpret the learned model