[[COMP26120]]

a ==spanning tree== is simply a tree which is acyclic and connects all nodes in the graph, at a minimum cost (where the cost is the ==sum of the weight of edges==)

### formalised
- say we have a connected and undirected graph $G = (V,E)$:
	- $V$ is the set of nodes to connect
	- $E$ is the set of possible interconnections
	- $E = \{(u,v)|w(u,v)\neq \infty\}$ where ==For all edges== ($(u,v) \in E$), $w(u,v) =$ cost of connecting $u$ and $v$

- The minimum spanning subtree of $G$ is an ==acyclic subset of edges== $T \subseteq E$ that ==connects all nodes== with the weight ==minimised==:
	- $W(T) = \sum_{(u,v)\in T)}w(u,v)$
- Therefore our problem at hand is determining this MST, $T$

### generic greedy algorithm to determine MST
in this algorithm, the MST grows by one edge at a time, but is not always globally optimal

```
procedure generic-MST(G,w)
	A = emptyset
	while A is not a spanning tree:
		find edge (u,v) that is safe for A
		A.add(u,v)
	return A //at this point A must be a spanning tree
```

- this while loop will execute $|V| - 1$ times, and the main challenge is finding a safe edge
- the correctness can be proved with a loop invariant, which is that $A \subseteq$ some MST

### safe edges
- as an example, we take an undirected graph as described above, $G = (V,E)$
- we take a subset of edges $A \subseteq E$ which is included in the MST for $G$
- we also take an arbitrary ==cut== of $G$ that ==respects== $A$ ([[cuts and light edges]]) - $(S,V-S)$
- now that we have a cut, we can find some ==light edge== which crosses $(S,V-S)$ - because we already know that this cut respects $A$, there are no edges which already cross the cut in $A$
- but we've now found some edge which has the minimum weight, and crosses the cut - we ==must== include this edge in $A$ because we are aiming to connect all nodes
- therefore we say this edge is ==safe for A==, because it has connected a new node in the MST we are trying to build, without introducing any cycles or redundant weight

### other MST building algorithms
- [[kruskals algorithm]]
- [[prims algorithm]]