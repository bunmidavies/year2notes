[[COMP24011]]

a [[tree decomposition]] is able to represent a graph as a tree. Multiple nodes from one graph are put into a ==bag==, and all the existing links within the original graph must occur between the bags in the tree
![](https://i.imgur.com/wKwAFyD.png)

the width of a tree-decomposition if the ==largest bag - 1==
original = left, tree decomposition = right
![](https://i.imgur.com/gC4i9Rz.png)

a graph with a tree width of 1 has ==no cycles==

tree width is useful to us because if a tree decomposition has width $k-1$, then the corresponding constraint network ==must have a solution== (given the graph is ==k-consistent== ([[k-consistency]]))