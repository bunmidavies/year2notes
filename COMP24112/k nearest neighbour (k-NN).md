[[COMP24112]]

### definition
k-NN is the ==simplest of all machine learning algorithms==, and dates back very early by a scientist in optics and perception (965-1040)

early academic works on k-NN start in the 60s

***
# k-NN classification
we'd like to construct a model which can classify objects into one of several known classes

example data = $\{x_i,y_i\}^n_{i=1}$
in this example data, $x$ is the ==feature vector==, and $y$ is the ==class label==

***
example: iris classification - a dataset contains 150 iris samples from 3 classes (setosa, versicolour and virginica) each characterised by ==sepal length== and ==petal width== measured. The goal of the model is to be able to predict the flower type of a query iris sample

this means the feature vectors are ==2-dimensional== - made of 2 measurements
***

==Classification Rule== with **majority voting**
```
classifiction(x,k)
	for each training data point xtr
		measure distance (x, xtr)
	sort distances
	select k nearest points
	return the most common class between these points
```
in short, the nearest neighbours from the point you are trying to classify are identified, sorted, and of the ==k== nearest neighbours, whichever class is most common among these is the class you think your point belongs to


***
# k-NN Regression
the example data and feature vectors take the same format as it is in k-NN classifcation, but instead of a class label, we simply have ==output== instead (refer to [[classification]] and [[regression]])

==Regression Rule==
```
regression(x,k)
	for each training data point xtr
		measure distance (x,xtr)
	sort distances
	select k nearest points
	output = (sum of k nearest points) / k
	return output
```

note that with k-NN regression, the model is ==not reliable== for predicting outputs outside of the range of the training inputs which we have provided

examples of k-NN regression: image completion/face recognition, sine wave point regression