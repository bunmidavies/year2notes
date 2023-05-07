[[COMP24112]]

### definition
- within [[clustering]], it was explained how the distance between two datapoints or samples can be calculated
- now, the question is how to measure the distance/similarity between ==two clusters themselves== - there are 3 main ways to do this as shown below

### single-link measure
- the single link measure involves calculating the ==minimum distance== between a data point in one cluster and a data point in the other cluster
![](https://i.imgur.com/7bfleWE.png)

### complete-link measure
- the complete link measure calculates the ==maximum distance== between two data points in two different clusters
![](https://i.imgur.com/7C7pi7o.png)

### average-link measure
- the average-link measure takes the distance between all data points in both clusters, and returns the mean
![|550](https://i.imgur.com/QjttOAo.png)
