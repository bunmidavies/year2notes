[[COMP24112]]

- classification models make use of [[discriminant function]]s, and these functions can be trained by minimising the ==sum-of-squares loss==
- this results in the least squares approach for classification

### least squares approach for binary classification
- binary classification = +1/-1 label coding (1 = class A, -1 = class B)
![](https://i.imgur.com/fnvJW6v.png)

### least squares approach for multi-class classification
- +1/-1 label coding can also be used for multiclass classification ($y_i = 1$ means the sample ==is== from the $i$th class)
![](https://i.imgur.com/iDyy5dg.png)

### iris classification example
![](https://i.imgur.com/JNWEYmT.png)

### general settings (i.e. not using +1/-1 label coding)

- thresholding by $T$ can be the discriminant function (where $T = (a+b)/2$)
- ==a/b label coding== can be used instead of +1/-1 label coding, where a nuber $a$ indicates the input is from class $i$, and $b$ indicates the input is NOT from class $i$ or just from some other class for binary classification
- any number can be picked for $a$ and $b$ as long as $a \neq b$
- ==for some data, the performance can be sensitive to the choice of a and b==

### hinge loss for classification
- hinge loss assesses classification error given +1/-1 label coding
![](https://i.imgur.com/lKrwqG5.png)
- there are 3 basic ways to classify the error based off this graph:
	1. if $a$ is greater than 1, there is ==no error==
	2. if $a$ is between 0 and 1, there is a ==small error==
	3. if $a$ is less than 0 (i.e. negative) there is a ==large error==
- as with regression loss, a ==regularisation term== and ==regularisation parameter== can be added
![](https://i.imgur.com/IAkeFup.png)

### hinge loss for binary classification example
![](https://i.imgur.com/uB1x10m.png)
