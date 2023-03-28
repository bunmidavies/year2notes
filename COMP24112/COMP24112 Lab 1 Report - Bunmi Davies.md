# Experiment 1

- The cosine distance implementation of KNN returns a mean accuracy of 0.962 over 20 trials (with a sample standard deviation of 0.00664) while the euclidean distance implementation of KNN returns a mean accuracy of 0.898 over 20 trials (with a sample standard deviation of 0.0185). This means the cosine distance KNN implementation performs better than euclidean distance KNN in terms of accuracy - cosine similarity (which is just 1 - cosine distance, as cosine distance is 1 - cosine similarity) is still able to classify vectors as similar which are far apart by euclidean distance, but have similar angles. This means that two documents which may be very different in size (number of words in the document), may still be similar in content, thus similar when using `cosine` (but not similar using `euclidean`).

# Experiment 2

- Within this experiment, after recording the errors from k=1 to k=50 for both training and testing, and comparing the errors side by side, as mentioned in the jupyter notebook the training accuracy was higher than the testing accuracy for 43 out of the 50 K values. This means that for the most part of the experiment, the classifier's training accuracy was better than the classifier's testing accuracy. The reason for this can attributed to the fact that to determine training accuracies, the same samples are used for both the training and testing of the model:
```python
training_result = knn_classify(data[training_samples],data[training_samples],labels[training_samples],"cosine",k)
```
- This means that samples which are shown to the classifier have already been taken into account within the model when performing distance measurement within the model, unlike when determining the testing accuracy of the model
```python
testing_result  = knn_classify(data[testing_samples],data[training_samples],labels[training_samples],"cosine",k)
```
- This is clearly using a different set of data to now test the classifier, so now when the classifier is only faced with unseen samples it is more likely to misclassify these test samples
- Within the experiment, as shown by the graphs it is clear to see that increasing K increases both the training and testing error of the model. In terms of bias and variance, the bias increases as K increases since many samples which may be in classes different to the class the chosen data point is in, will start to be considered as neighbours, resulting in a higher chance of incorrect classifications made by the model. This also means that the lowest k (k=1) has the lowest error, and lowest bias since the 'noise' within the datas can be visualised as being perfectly memorised by the model. Potential noise also being modelled means that the variance within the model is at its highest when k=1, and decreases as k increases - the model becomes more 'general' and less suceptible to modelling noise, but as mentioned before has a bigger chance of incorrect classification (higher bias).

# Experiment 3

- Based on the content of the new 5 articles, it seems unclear as to which classes these articles should belong to. Judging from some of the content in the already existing articles, it appears that some of the articles may have some relation to finance related topics - but it is unclear of what the class names 'earn', 'crude', 'trade', and 'interest' exactly mean, and for this reason it does not feel as if a logical judgement can be made as to which classes these new articles belong to.
- Due to it being unclear as to what classes these articles should belong to (as explained above), the question of whether the classifier can make appropriate class predictions for these 5 articles becomes inapplicable. There is no concept of an appropriate class prediction since there is no appropriate class which the new articles belong to.
- As shown within the report, the accuracy for classes 0 to 3 all lie above the 0.95 mark, while the accuracy for the 'sports' class i.e. class 4 is 0.417. This shows that the main consequence of having limited data for the 'sports' class is that since only 2 sports documents are ever provided within testing, the accuracy can only ever be 0, 0.5 or 1 (which then gets averaged across a number of trials resulting in the avg. accuracy recorded). This means that the 'sports' class will typically appear to have much worse performances than the other classes, and this is a result of the limited data for not only training, but for testing as well.

- Explanation of zero-shot learning and few-shot learning in the concept of this lab:
	- Zero-shot learning is the idea of a model predicting the correct class of an article without being trained with any singular article which belongs to that class. We would be implementing zero-shot learning if instead of providing 3 sports articles for training, we provided 0 sports articles for training and tried to classify all 5 of the sports articles (while still including the 'sports' class in the classifier, just providing no examples for it)
	- Few-shot learning is the idea of a model aiming to predict the correct class of an article while being trained by a very small number of examples from that class. Experiment 3 is performing few-shot learning with the sports class - we only provide 3 example sports articles in comparison to the 80 example articles for all other classes.

# Analysis 1

- Computing the confidence interval in either direction involves the following formula:
  $$a = z_p \sqrt{\frac{error_s(1-error_s)}{n}}$$
- where $error_s$ is the sample test error (i.e. the error we calculate after running the KNN classifier on the provided test samples), $n$ is the number of samples we tested the classifier with, and $z_p$ is a constant based on our confidence level, which we want to be 90% (as the notebook tells us we want the interval where the true error lies with 90% probability). This calculation with values plugged in can be viewed in the notebook

# Analysis 2

- After performing the training-testing trials for k=45 and comparing it with k=1, we find that k=45 has a testing sample error of 0.0648 while k=1 has a testing sample error of 0.0352. We then perform a z-test with the hypothesis that k=45 has a higher true test error than k=1. We calculate $z_p$ first with the following equation:
$$z_p = \frac{|\textrm{error}_{s1}(A) - \textrm{error}_{s2}(B)|}{\sqrt{\frac{\textrm{error}_{s1}(A)[1-\textrm{error}_{s1}(A)]}{n_1} + \frac{\textrm{error}_{s2}(B)[1-\textrm{error}_{s2}(B)]}{n_2}}}$$
- where in this context $\textrm{error}_{s1}(A)$ is the testing sample error for k=45, and $\textrm{error}_{s2}(B)$, and $n_1$/$n_2$ are both the fixed value of 320 since 320 testing samples are used for both implementations of the KNN classifier
- once $z_p$ is known, the `Get_p_value` function provided within the notebook can be used with the $z_p$ value as a parameter, and the final probability is returned. In the notebook this p value comes out to be 0.91, meaning that it can be said with a 91% confidence level that our hypothesis (the testing true error for k=45 is higher than the testing true error for k=1) is true.

# Hyperparameter Selection

- For the following experiment I firstly chose to split the training+validation and test data to 75% and 25% of the data respectively - internally within the training trials, the training data was 2/3 of the data and the remaining 1/3 was for validation. The main reasoning behind this strategy was to ensure there was both a sufficient amount of training, testing and validation data. This allows meaningful conclusions to be drawn from validation and testing since there is enough data to do so. But the splitting also ensures that there is more training data than validation/testing to allow the model to have as much data as possible to learn from, so that the model can provide statistically significant results, and allow realistic conclusions to be drawn to select a hyperparameter.
- Using the training/validation data, I performed random subsampling - within each trial for each k value, 400 of the 600 samples were randomly selected for training, and the remaining 200 samples were used for validation
- 20 trials were ran in total for each k value, from k=1 to k=50. The average errors and their standard deviations were calculated, and plotted using matplotlib
- The model to be selected for final evaluation was the model with the lowest averaged test sample error. A single trial of training/testing was then performed on the selected model and reported within the notebook.
![ | 350](https://i.imgur.com/cG6qO8a.png)
- As can be seen within the graph, k=1 has the lowest averaged test sample error, meaning the model with this hyperparameter setting is selected as the model for final evaluation. The final evaluation is then carried out on the model with k set to 1 within the jupyter notebook.
- There are multiple reasons as to why it is important to split the data into training, validation and testing sets when performing machine learning experiments. Firstly, by having a training/validation split, this helps with preventing overfitting. Overfitting occurs when a model performs well on the data it is trained on, but poorly on unseen data. By testing each of the k values with validation data in the training phase, we ensure we select a k value which can generalise well to new data. This is further strengthened by then having a completely separate testing set. This testing set is able to provide an unbiased estimate of the models performance on completely unseen data.