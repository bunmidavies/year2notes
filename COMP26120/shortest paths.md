[[COMP26120]]

The shortest path with BFS from node $s$ to some node is the ==minimal== number of edges

To obtain the path once the target node has been found, a ==predecessor map== is used - this stores the nodes from which any node was discovered

```
shortestPath(s)
	D <- [s], F <- emptyset, pre(s) <- s
	while D is not empty do
		u <- D.pop()
		F <- F and {u}
		for all undiscovered neighbours of u
			D.push(neighbour)
			pre(neighbour) <- u
	return pre
```

`pre` at this point will now store the information required to retrieve the shortest path:

```
getPath(pre, u)
	p <- [u]
	while pre(u) != u do
		u <- pre(u), p <- up //u concatenated onto p
	return p
```

