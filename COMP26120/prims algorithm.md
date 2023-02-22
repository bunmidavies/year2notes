[[COMP26120]]

- prims extends the generic greedy approach covered in [[minimum spanning trees]], and takes an approach that is somewhat similar to [[dijkstras algorithm]]

### pseudocode
```
procedure MST-Prim(G,w,r)
	for each node u
		u.key = infinity
		u.parent = null
	r.key = 0
	Q = V // Q = nodes in G
	while Q isnt empty
		u = extract-min(Q)
		for each edge (u,v) with weight w(u,v) != infinity
			if v in Q and w(u,v) < v.key
				v.parent = u // set new parent
				v.key = w(u,v) // set new minimum
```

- the algorithm starts from any given node $r$ (argument to the function), then in each step, adds a ==light edge== to $A$, that connects $A$ to an isolated vertex
- v.key is the ==minimum weight== of any edge connecting v to a node in the tree, i.e. the current ==light edge== which the algorithm has found ([[cuts and light edges]])
- $Q$ is a minimum priority queue, using key
- u.parent = the parent of u in the tree, it is also written as $u.\pi$ in the lectures
- $A = \{(v,v.parent) : v \in V - \{r\} - Q\}$
- the while loop executes $|V|$ times

![](https://i.imgur.com/JnJ5Nqu.gif)


### complexity
- similar to how [[kruskals algorithm]] depends on the implementation of the data structures it uses, prims also depends on the implementation of the minimum priority queue $Q$
- using a fibonnaci heap, the complexity comes to $O(|E| + |V| log |V|)$