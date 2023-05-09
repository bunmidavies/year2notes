[[COMP24112]]

### ~ euclidean distance
- the most commonly used method for distance is ==euclidean distance==
$$d(p,q) = \sqrt{\sum^d_{i=1}(p_i-q_i)^2}$$


### ~ minkowski distance
- ==minkowski distance== is a more generalised form of euclidean distance, and is able to give different types of distance based on a parameter $t$
$$d(p,q) = [|p_1-q_1]^t + |p_2 - p_1|^t + ... + |p_d - q_d|^t]$$
this turns into:
$$d(p,q) = \left[\sum^d_{i=1}|p_i-q_i|^t \right]^{\frac{1}{t}}$$
- where $d$ is the no of dimensions in the vectors, and $t$ is a parameter you decide
	- $t$ = 2: euclidean distance
	- $t$ = 1: manhattan distance

### ~ inner product
==similarity measurement== can also be used. The k nearest neighbours in this case have to have the highest similarity values

inner product:
$$s_{inner}(p,q) = \sum^d_{i=1}p_iq_i = p^Tq$$

### ~ cosine distance + cosine similarity
cosine similarity:
$$\frac{p^Tq}{\sqrt{\sum^d_{i=1}p^2_i} \cdot \sqrt{\sum^d_{i=1}q^2_i}}$$
$$\frac{\textrm{inner product}}{\textrm{euclid. norm of p}\cdot\textrm{euclid. norm of q}}$$

- cosine distance = $1 - \textrm{cosine similarity}$
