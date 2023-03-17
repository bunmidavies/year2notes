[[COMP24112]]

### Holdout Method
- Split the dataset into a ==training set== and a ==test set== - and use them accordingly (i.e. training with the training set, and estimating model error with the test set)
- A common disadvantage of the holdout method is that if the dataset is small, it is had to split this dataset into a testing and training set
- As well as this, the estimate of error rate can be misleading if there is an 'unfortunate' split - i.e. the sample error isn't close to the true error

### Random Subsampling
- Kind of like a more advanced version of the holdout method, where $K$ data splits are performed on the entire dataset. Each split randomly selects a fixed number of samples for testing, and uses whatever is left for training
- For each data split, the classifier is trained from scratch using the training samples, and the error rate is estimated with testing samples
![](https://i.imgur.com/gBlKU0W.png)


### K-fold Cross Validation
- Divide the entire dataset into $K$ partitions, then for each of the $K$ experiments, use $(K-1)$ partitions for training and the remaining for estimating the error rate
- The advantage of this is that all the examples in the dataset sooner or later will be used for both training and testing
- In the image below, the (K-1) partitions would basically be the white section, then the remaining partition is the grey section, used for estimating $E_i$ (error rate)
![](https://i.imgur.com/FcXYTPb.png)

- A low number of $K$ will result in insufficient training-testing trials, while a high number of $K$ might result in a small testing set, which can potentially cause high variance
- Typical settings for $K$ are within 5-10

### Leave One Out (LOO)
- A special case of K-fold Cross Validation
- Given $N$ samples, LOO is ==N-fold Cross Validation== - this is suitable for a small sample set (because as said above, $K$ is typically 5 or 10)

### Bootstrap
- Bootstrapping is based on ==sampling with replacement==
- The following process is repeated $K$ times:
	- Randomly select (with replacement) $M$ samples and use these for training
	- The samples which ==weren't selected== are for testing - the number of testing samples can change over repeats
![](https://i.imgur.com/EWM4OWu.png)

- The main difference between this and random subsampling above is that the actual sampling method is different - for bootstrapping, you put the sample back into the set after selecting it (meaning it is possible to have ==duplicates==)