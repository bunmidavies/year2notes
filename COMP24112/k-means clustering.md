[[COMP24112]]

### definition
- k-means clustering is the simplest and most frequently used clustering algorithm
- it was first introduced by stuart lloyd in 1957 (referred to as lloyd algorithm) - the actual term 'k-means' was introduced by james macqueen in a paper, in 1967

### k-means clustering steps
- in order to group a set of data points into $k$ clusters, the following steps are taken:
1. pre-determine the cluster number $k$
2. choose a distance/similarity measure
3. select $k$ random cluster centre points (typically random datapoints you're trying to cluster?)
4. repeat the following
	1. calculate distances/similarities between data points and cluster centre points
	2. find the ==nearest== cluster centre to each data point, and assign that cluster to the data point
	3. calculate the ==new cluster centre== for each cluster, by averaging the assigned data points
	4. ==repeat steps 1-3 until one iteration results in no change in cluster membership==

### comments / issues with k-means
- the k-means process is mathematically equivalent to solving a minimisation problem, with a sum of squares cost:
$$\textrm{min}\sum_{i=1}^{K}\sum_{p\in\textrm{cluster i}} d^2(x_p, c_i)$$
- where $c_i$ is the centre vector of cluster $i$, and $x_p$ belongs to cluster $i$
- this problem will always converge, but can converge to an ==unwanted solution==
- k-means has a few cons:
	- the algorithm is sensitive to the initial cluster centre points
	- the number of clusters must be specified in advance, so in cases when you dont actually know how many there should be, there can be problems
	-  the algorithm cant handle noisy data/outliers, thus isnt suitable to discover clusters for complex data patterns