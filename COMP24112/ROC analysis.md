[[COMP24112]]

### definition
- ROC stands for ==receiver operating characteristic==
- ROC analysis involves trying different thresholds, $T$, in a [[discriminant function]] for a binary classifier, to observe how performance changes for different values of $T$
- for each threshold value, different pairs of measurements can be collected:
	- 1-specificity and sensitivity (i.e. recall)
	- false positive rate and true positive rate
- an ROC curve plots the above measurements against eachother, for different values of $T$

### example plot
![](https://i.imgur.com/P7aFwWg.png)
- the green box basically explains that since the x axis is the false positive rate, when the x axis is on 0 the false positive rate must be 100, therefore the true positive rate has to be 0
- likewise the red box explains that since the true positive rate is 100%, the true negative rate drops to 0

### balance of ROC curves
- the ==balance== of an ROC curve can be measured by calculating the ==area under the curve (AUC)== - the closer this area is to 1, the better
![](https://i.imgur.com/9Ghgc8g.png)
