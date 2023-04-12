[[COMP24011]] - [[constraint satisfaction problems]]

a ==cycle cutset== in an undirected graph is a set of nodes whose removal results in a graph with ==no cycles==

say $X$ is a cycle cutset in a graph for a constraint network - by trying all possible values for the variables in $X$ we can obtain a ==backtrack-free== network in the graph without $X$

it is a difficult problem to find cycle cutsets, but algorithms exist to do this

a [[tree decomposition]] is able to represent a graph for a constraint network using ==bags== which represent groups of nodes within this original graph