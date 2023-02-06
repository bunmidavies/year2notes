[[COMP26120]]

==generic graph traversal algorithm==:
- Explore edges to new nodes, until all nodes discovered
- Create sets as you go:
	- $D$: discovered, outgoing edges yet to be explored
	- $F$: finished, outgoing edges which have been explored

```
explore(s):
	//initialise
	D <- {s}, F <- emptyset

	//main loop (non iterative)
	while D != emptyset do
		u <- Some u in D
		D <- D and (All successors of u that arent in F)
		D <- D \ {u}
		F <- F and {u}
	return F
```

`explore` returns all the nodes which are reachable from $s$ - if the node is reachable, it'll be included in $F$

BFS and DFS use this generic algorithm, but the order in which it explores nodes differs - this is due to the data structures used for each implementation:
- DFS = ==stack==
- BFS = ==queue==

DFS can be implemented ==recursively==, without actually using a stack:
```
DFS(F,u):
	if u not in F then
		F <- F and u
		for all v with (u,v) in E do //for all successors of u
			F <- DFS(F,v)
	return F
```