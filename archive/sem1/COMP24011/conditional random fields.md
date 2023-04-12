[[COMP24011]] / #comp24011 

CRFs are similar to HMMs ([[probabilistic models]]), with some differences

HMMs are considered ==generative== - they can detect attributes, but also generate some text containing this same attribute

for [[information extraction]] though, this second property isn't really useful, so we want a ==discriminative model== - something that models the probability of hidden states given observations

==CRFs find the most probable label sequence y given an observation sequence x==

Example: consider the following observation sequence:
*There will be a seminar by Dr Andrew McCallum on Friday*

CRFs will predict the most likely sequence, consisting of which attribute it thinks each observation belongs to

$$y = \textrm{argmax}_y p\lambda(y|x)$$

this means the sequence $y$ is the sequence with the ==max probability== given $x$

$$p_\lambda(y|x)=\frac{1}{Z_x}\cdot exp(\sum_{i=1}^n\sum_{j=1}^{m}\lambda_jf_j(y_{i-1},y_i,X,i))$$

- $Z_X$ - normalisation factor
- $\lambda$ - weight
- $f_j$ - feature function

a ==feature function== characterises input - different functions exist for different features e.g. is the word all capitalised? all digits? 
feature functions are useful for ==named entity recognition==

![](https://i.imgur.com/N0vvPw0.png)
