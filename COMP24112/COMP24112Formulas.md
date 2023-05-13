# maths doc
### matrix multiplication
- $X$ has dimensions $m \times n$
- $Y$ has dimensions $n \times p$
- $XY$ will have dimensions $m \times p$
$$(XY)_{ij} = \sum^n_{k=1}X_{ik}Y_{kj}$$
### inner product
- given two $n$-dimensional column vectors $x$ and $y$
$$x^Ty = \sum_{i=1}^nx_iy_i$$
### euclidean norm
- also known as the $l_2$ norm
- the frobenius norm for matrices follows the same idea, but iterates over all rows/cols
$$||x||_2 = \sqrt{\sum_{i=1}^nx_i^2} = \sqrt{x^Tx}$$

# chapter 1
- no formulas

***
<div style="page-break-after: always;"></div>

# chapter 2
- $d$ = no of dimensions in the vectors
### euclidean distance
$$d(p,q) = \sqrt{\sum^d_{i=1}(p_i-q_i)^2}$$


### minkowski distance
$$d(p,q) = \left[\sum^d_{i=1}|p_i-q_i|^t \right]^{\frac{1}{t}}$$
- $t$ = 2: euclidean distance
- $t$ = 1: manhattan distance

### cosine similarity + cosine distance
- cosine similarity:
$$\frac{p^Tq}{\sqrt{\sum^d_{i=1}p^2_i} \cdot \sqrt{\sum^d_{i=1}q^2_i}}$$
$$\frac{\textrm{inner product}}{\textrm{euclid. norm of p}\cdot\textrm{euclid. norm of q}}$$

- cosine distance = 1 - cosine similarity

***
<div style="page-break-after: always;"></div>

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

***
<div style="page-break-after: always;"></div>

# chapter 4
### conditional mean for regression + probabilistic inference
$$\hat{y} = E_f[f|x]$$
### logistic sigmoid
$$f(x) = \frac{1}{1+e^{-x}}$$
### softmax function
$$\textrm{softmax}(x_i) = \frac{e^{x_i}}{\sum^c_{j=1}e^{x_j}}$$ 

***
<div style="page-break-after: always;"></div>

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
$$-\sum^N_{i=1}\left[y_i\log_b(p(c_1|x_i))+(1-y_i)\log_b(p(c_2|x_i))\right]$$
### cross entropy loss (multi-class classification)
- $b$ is either $e$, so you're using $\ln$, or 2
$$-\sum^N_{i=1}\sum^c_{k=1}y_{ik}\log_b(p(c_k|x_i))$$

### MLE (binary classification)
- consider the i-th training sample to be $(x_i,y_i)$
$$L = \theta(x_i)^{y_i}(1-\theta(x_i))^{1-y_i}$$

### MLE (multi-class classification)
- $y_{ik}$ will either be 1 or 0, and for any given sample, only one $k$ will have $y_{ik}$ of 1 (since multi-class classification is assigning ==one== of many labels) 
$$L = \prod_{i=1}^{N}\prod_{k=1}^{c} \theta_k(x_i)^{y_{ik}}$$
***
<div style="page-break-after: always;"></div>

# chapter 6

### gradient descent (general)
$$w^{(t+1)} = w^{(t)} - \eta\sum^N_{i=1}\nabla O_i(w^{(t)})$$
### stochastic gradient descent (general)
- $i$ is a randomly chosen sample
$$w^{(t+1)} = w^{(t)} - \eta\nabla O_i(w^{(t)})$$
### minibatch gradient descent (general)
- use a subset of all training samples, $n$
$$w^{(t+1)} = w^{(t)} - \eta\sum^N_{n\in N}\nabla O_i(w^{(t)})$$
***
<div style="page-break-after: always;"></div>

# chapter 7

### neuron activation (sigmoid)
$$y = \varphi(\sum_{i=1}^dw_ix_i + b)$$

### ReLU function
$$\varphi(v) =
    \begin{cases}
      v & \text{\textit{if } v $\geq$ 0}\\
      0 & \text{\textit{if } v $<$ 0}
    \end{cases}  
$$

### hebbian learning rule
- *within examples in 7B - $z_j$ refers to ==ground truth== values - not fully clear how this differs to perceptron*
$$w^{(t)}_{ij} = w^{(t-1)}_{ij} + \eta x_iz_j$$

### perceptron criterion
$$O(w) = - \sum_{i\in\text{Misclassified set}} y_i(w^T\tilde{x}_i)$$

### perceptron algorithm
- the update is performed using a misclassified sample
$$w^{(t)}_{ij} = w^{(t-1)}_{ij} + \eta y_i\tilde{x}_i$$

### chain rule
- assume z takes the argument $y(x)$ (or think of it as $u$, a singular term)
$$\frac{dz}{dx} = \frac{dz}{dy} \times \frac{dy}{dx}$$

### general derivative of cost for backpropagation
- [3blue1brown vid](https://www.youtube.com/watch?v=tIeHLnjs5U8)
- $O$ = loss function
- $w$ = weight we are trying to update
- $a$ = activation of neuron sum (i.e. sigmoid function)
- $z$ = neuron sum (before sigmoid is applied)
- the activation and neuron sum are separated to allow for use of the chain rule
$$\frac{\partial O}{\partial w^L} = \frac{\partial z^L}{\partial w^L} \cdot \frac{\partial a^L}{\partial z^L} \cdot \frac{\partial O}{\partial a^L}$$
***
<div style="page-break-after: always;"></div>

# chapter 8

### separation margin between SVM hyperplanes
$$\frac{2}{||w||_2}$$

### support vectors
- not really a formula, just a point that support vectors $y$ in an SVM satisfy the following
$$y_i(w^Tx_i + b) = 1$$
***
<div style="page-break-after: always;"></div>

# chapter 9

- for cluster measures assume:
	- $p \in \text{cluster}_i$
	- $q \in \text{cluster}_j$

### single-link measure
$$d(\text{cluster}_i,\text{cluster}_j) = \text{min } d(x_p,x_q)$$

### complete-link measure
$$d(\text{cluster}_i,\text{cluster}_j) = \text{max } d(x_p,x_q)$$

### average-link measure
$$d(\text{cluster}_i,\text{cluster}_j) = \frac{1}{n_in_j}\sum d(x_p,x_q)$$

### within-cluster sum of squares
- also known as within-cluster variance
- assume $K$ clusters, and $c_i$ to be the centre of $i$-th cluster
$$SSW = \sum_{i=1}^K\sum_{p\in\text{cluster}_i}d^2(x_p,c_i)$$

### between-cluster sum of squares
- also known as between-cluster variance
- $c$  = whole data centre (average out all points from all clusters)
- $n_i$ = number of data points in $i$-th cluster
$$SSB = \sum_{i=1}^Kn_id^2(c_i,c)$$

### f-ratio index
$$F = K \frac{SSW}{SSB}$$

### rand index
- $a$ = no of pairs from the same class and cluster
- $b$ = no of pairs from different classes but same clusters
- $c$ = no of pairs from the same class but different clusters
- $d$ = no of pairs from different classes and different clusters
$$Rand = \frac{a+d}{a+b+c+d}$$

### rand index values
- cant be bothered to write these out
![](https://i.imgur.com/ZoXIq5S.png)
***
<div style="page-break-after: always;"></div>

# chapter 10

### activation map resultant size
- $N_1$ = input layer width
- $N_2$ = input layer height
- $F_1$ = convolutional filter width
- $F_2$ = convolutional filter height
- $S$ = stride size
$$(\frac{N_1-F_1}{S}+1)\times(\frac{N_2-F_2}{S}+1)$$