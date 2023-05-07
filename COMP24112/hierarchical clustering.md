[[COMP24112]]

### definition
- hierarchical clustering works by grouping objects into ==trees of clusters==, which results in nested partitions layer by layer
- for this reason no cluster number needs to be known in advance
- there are two main hierarchical strategies which are covered below - the picture below showing the results of hierarchical clustering is known as a ==dendogram==

![| 550](https://i.imgur.com/VcMeGTq.png)

### agglomerative (bottom-up)
- the agglomerative algorithm can be summarised in 3 steps:
1. start with each data point being its own cluster (==atomic clusters==)
2. merge these clusters together to gain larger and larger clusters
3. repeat steps 1-2 until there is a ==singular cluster remaining==
- in order to select the two closest clusters to merge, use either single-link, complete-link, or average-link ([[cluster distance measures]])
- the lifetimes of these clusters can be shown using a graph, and the lifetime itself is just the distance difference between where it was created, and the cluster it merged with
![|650](https://i.imgur.com/tf1hpst.png)
- now, by using a ==distance threshold==, you can decide which clusters y ou actually end up with
- the major drawbacks to the agglomerative algorithm are that like k-means, its sensitive to noise/outliers, but is also less efficient than k-means ($O(N^2logN)$)


### divisive (top-down)
- start by treating all data points as ==one single cluster==
- divide this cluster into smaller and smaller clusters