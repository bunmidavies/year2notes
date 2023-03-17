[[COMP24112]]

as already mentioned, [[classification]] consists of:
- samples : ${x_i,y_i}$
- a feature vector : $x_i \in R_d$ (the ==input==)
- a class label : $y_i \in \{1,2,...,c\}$ (the ==output==)

there are different methods of measuring how well a classifier actually performs


### classification accuracy / error
classification accuracy and error rates are quite simple:
- accuracy rate = number of correctly classified samples $\div$ total sample number
- error rate = number of wrongly classified samples $\div$ total sample number

there are certain reasons why these measures aren't always used:
- ==unbalanced data== makes accuracy/error unreliable
- accuracy/error cannot tell ==classifier behaviours== i.e. certain classifiers may work better for certain classes

### confusion matrix
a common type of confusion matrix is the ==error matrix==- each row represents samples in a predicted class, while each column represents samples in an actual class
![](https://i.imgur.com/WNWeOXG.png)


==a confusion matrix is always 2x2, and can be created from the above matrix==

![](https://i.imgur.com/C4M5GQr.png)


this is like the regular confusion matrix seen in [[COMP24011]], where you essentially have matching class + included in result set, matching class + not included, wrong class + included, and wrong class + not included

***
from this, ==precision== and ==recall== can be calculated for assessing the ability to classify ==positive== samples:
- Recall = True positives $\div$ Number of real positives 
- Precision = True positives $\div$ Number of predicted positives
Remember that the numerator for both equations is always the same - the true positives. For recall remember that it is concerned with which of the correct results have been ==recalled==, meanwhile precision is concerned with whether there have been wrongly identified features, i.e. how ==precise== a classifier is

==Recall is also known as sensitivity and true positive rate (TPR)==

$F_1 = 2PR / (P+R)$
***

***
==specificity== assesses the capability to classify ==negative== samples - 1-specifity is called ==false positive rate==
- Specificity = True negatives $\div$ Number of real negatives
- 1-Specificity = False positives $\div$ Number of real negatives