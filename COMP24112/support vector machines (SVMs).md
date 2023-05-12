[[COMP24112]]

### definition
- the original idea of an SVM was introduced by the generalised portrait algorithm (Vapnik and Lerner) in 1963
- SVMs themselves were formally introduced in 1992
- in short, an SVM is a [[supervised learning]] algorithm, which takes a set of data points to find an ==optimal hyperplane== to separate (ideally) two classes of data points, with the ==widest margin== possible (using 2 hyperplanes)
- [[hyperplanes in linear functions]] covers what a hyperplane is, as well as the separation margin

### hard-margin SVM
- ==hard-margin SVM== finds an optimal hyperplane which fully separates two classes of data points, and has the widest margin
- it does so by solving a ==constrained optimisation problem==:
	- finding the minimum value from $\frac{1}{2} w^Tw$
	- while ensuring that $y_i(w^Tx_i + b)\geq 1 \forall i \in \{1,...,N\}$
- that optimisation problem is converted to a ==dual problem==, which by solving, will give you the answer to the original problem
![](https://i.imgur.com/vddFofO.png)
- dual problems are known as ==quadratic programming== problems - solving these is optional reading
- $\lambda_i$/$\lambda_j$ is known as a ==Lagrangian multiplier== - it should be a positive number, and it has a fixed relationship with $w$ and $b$

### support vectors
- support vectors are training points which lie on the upper / lower hyperplanes which are created 
- mathematically, these points satisfy the equation: $y_i(w^Tx_i + b) = 1$
- these points are the most difficult to satisfy when determining the hyperplanes, and have much more impact on where they actually end up in comparison to the further away points

### links
- [SVM history](http://www.svms.org/history.html)