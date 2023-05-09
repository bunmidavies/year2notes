[[COMP24112]]

# chapter 1
- no formulas

# chapter 2
- $d$ = no of dimensions in the vectors
### ~ euclidean distance
$$d(p,q) = \sqrt{\sum^d_{i=1}(p_i-q_i)^2}$$


### ~ minkowski distance
$$d(p,q) = \left[\sum^d_{i=1}|p_i-q_i|^t \right]^{\frac{1}{t}}$$
- $t$ = 2: euclidean distance
- $t$ = 1: manhattan distance

### ~ inner product
$$s_{inner}(p,q) = \sum^d_{i=1}p_iq_i = p^Tq$$

### ~ cosine similarity + cosine distance
- cosine similarity:
$$\frac{p^Tq}{\sqrt{\sum^d_{i=1}p^2_i} \cdot \sqrt{\sum^d_{i=1}q^2_i}}$$
$$\frac{\textrm{inner product}}{\textrm{euclid. norm of p}\cdot\textrm{euclid. norm of q}}$$

- cosine distance = 1 - cosine similarity

# chapter 3
### classification accuracy / error
- accuracy:
$$\frac{\textrm{no. of correctly classified samples}}{\textrm{total sample number}}$$
- error:
$$\frac{\textrm{no. of wrongly classified samples}}{\textrm{total sample number}}$$
### recall and precision
- recall:
$$\frac{\textrm{true positives}}{\textrm{true positives + false negatives}}$$
$$\frac{\textrm{true positives}}{\textrm{no. of real positives}}$$
- precision:
$$\frac{\textrm{true positives}}{\textrm{true positives + false positives}}$$
$$\frac{\textrm{true positives}}{\textrm{no. of predicted positives}}$$
### specificity + 1-specificity
- specificity:
$$\frac{\textrm{true negatives}}{\textrm{true negatives + false positives}}$$
$$\frac{\textrm{true negatives}}{\textrm{no. of real negatives}}$$
- 1-specificity (false positive rate):
$$1 - \frac{\textrm{true negatives}}{\textrm{true negatives + false positives}}$$
$$\frac{\textrm{false positives}}{\textrm{no. of real negatives}}$$
### mean square error (MSE)
- formulas assume given $n$ samples and a single output for each ($\hat{y}$)
$$\frac{1}{n}\sum^n_{i=1}(y_i-\hat{y}_i)^2$$
### root mean square error (RMSE)
$$\sqrt{\frac{1}{n}\sum^n_{i=1}(y_i-\hat{y}_i)^2}$$
### mean absolute error (MAE)
$$\frac{1}{n}\sum^n_{i=1}|y_i-\hat{y}_i|$$
### mean absolute error (MAPE)
$$\frac{1}{n}\sum^n_{i=1}\frac{|y_i-\hat{y}_i|}{|y_i|}$$
### coefficient of determination
- aka proportion of the variance / $R^2$ score
$$1-\frac{\sum^n_{i=1}(y_i-\hat{y}_i)^2}{\sum^n_{i=1}(y_i - \bar{y})^2}$$
- $\bar{y}$ is the mean, aka
$$\frac{1}{n}\sum^n_{i=1}y_i$$
### confidence interval
$$a = z_p\sqrt{\frac{\textrm{error}_s(1-\textrm{error}_s)}{n}}$$
- $z_p$ values for two-sided confidence intervals:

| confidence level: p | 50%  | 68%  | 80%  | 90%  | 95%  | 98%  | 99%  |
| ------------------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| constant: $z_p$     | 0.67 | 1.00 | 1.28 | 1.64 | 1.96 | 2.33 | 2.58 |
- confidence interval is represented as $[\textrm{error}_s-a,\textrm{error}_s+a]$

### $z_p$ in z-test
$$z = \frac{d}{\sigma}$$
- $d = |\textrm{error}_{s1}(A) - \textrm{error}_{s2}(B)|$, where classifier A sample error > classifier B sample error
$$\sigma = \sqrt{\frac{\textrm{error}_{s1}(A)[1-\textrm{error}_{s1}(A)]}{n_1}+\frac{\textrm{error}_{s2}(B)[1-\textrm{error}_{s2}(B)]}{n_2}}$$
# chapter 4
### conditional mean for regression + probabilistic inference
$$\hat{y} = E_f[f|x]$$
### logistic sigmoid
$$f(x) = \frac{1}{1+e^{-x}}$$
### softmax function
$$\textrm{softmax}(x_i) = \frac{e^{x_i}}{\sum^c_{j=1}e^{x_j}}$$ 
# chapter 5
### sum of squares error (single-output)
- the $\frac{1}{2}$ exists to make differentiation easier (?)
$$\frac{1}{2}\sum^n_{i=1}(y_i-\hat{y}_i)^2$$
### sum of squares error (multi-output)
- the $\frac{1}{2}$ exists to make differentiation easier (?)
$$\frac{1}{2}\sum^n_{i=1}\sum^c_{j=1}(y_{ij}-\hat{y}_{ij})^2$$
### regularised linear least squares
- sum of squares error + regularisation term
$$\frac{1}{2}\sum^n_{i=1}(y_{i}-\hat{y}_{i})^2 + \frac{\lambda}{2}\sum^{d+1}_{j=1}w_j^2$$
### regularised linear least squares (linear model)
- sum of squares error + regularisation term
- reformatted using weight vector, for the single-output case
$$\frac{1}{2}\sum^n_{i=1}(y_{i}-w^T\tilde{x}_i)^2 + \frac{\lambda}{2}w^Tw$$
### hinge loss for binary classification
$$\sum^N_{i=1}\textrm{max}(0,1-y_if(\theta,x_i))$$

### cross entropy loss (binary classification)
- $b$ is either $e$, so you're using $\ln$, or 2
$$-\sum^N_{i=1}\left[y_i\log_b(p(c_1|x_i))+(1-y_i)\log_b(c_2|x_i))\right]$$
### cross entropy loss (multi-class classification)
- $b$ is either $e$, so you're using $\ln$, or 2
$$-\sum^N_{i=1}\sum^c_{k=1}y_{ik}\log_b(p(c_k|x_i))$$

### likelihood (binary classification)
- consider the i-th training sample to be $(x_i,y_i)$
$$p(x_i,y_i|\theta) = \theta(x_i)^{y_i}(1-\theta(x_i))^{1-y_i}$$
# chapter 6

# chapter 7
*revision week - no new content*

# chapter 8

# chapter 9

# chapter 10
