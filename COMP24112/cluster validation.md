[[COMP24112]]

### definition
- after performing some version of clustering, its important to evaluate the quality and the validity of the clusters which have actually been generated
- cluster validation is the process of using both ==internal criteria== and ==external criteria== to validate whether the clusters make sense
	- ==internal criteria== = 'common sense'
	- ==external criteria== = using 'ground truth'

### internal validation
- typically, a good clustering result should have a small within-cluster variance, while also having a large between-cluster variance (i.e. the distance between the actual clusters)
	- within-cluster variance (SSW) = $\sum^K_{i=1}\sum_{p\in\textrm{cluster}_i} d^2(x_p,c_i)$
	- between-cluster variance (SSB): $\sum^K_{i=1}n_id^2(c_i,c)$
	- F-ratio index: $K \cdot \frac{SSW}{SSB}$
- using the above measures, the cluster number i.e. $K$ can also be selected

### external validation
- external validation involves using 'ground truth' class labels of the data points - i.e. what clusters the data points could ==actually== belong to - this essentially gives you 2 partitions: the actual clustering you've created, and what class labels each of the data points belong to
- some problems may surround this:
	- the partitions may have a different number of clusters and classes, therefore they aren't directly comparable
- the ==rand index== is commonly used to compare these two partitions, through an ==agreement/disagreement table== 
![|650](https://i.imgur.com/A4VeB25.png)
- the rand index can also be computed from a contingency table
![|650](https://i.imgur.com/aYpg0LM.png)
