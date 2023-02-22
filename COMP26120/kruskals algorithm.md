[[COMP26120]]

- kruskals algorithm is a kind of extension of the generic greedy MST building algorithm (covered in [[minimum spanning trees]]) - in the generic algorithm we picked any edge which was safe at the time and added it to our MST, but kruskals works differently, using [[disjoint sets]]

### pseudocode

``` 
procedure MST-kruskal(G,w)
	A = emptyset
	for each node in G
		make-set(v)
	for each edge (u,v) ordered by weight ascending
		if find-set(u) != find-set(v)
			A.add((u,v))
			union(u,v)
	return A
```

- ==in kruskals, the edges are ordered by weight== - you pick the smallest one, and if they're connecting two nodes together which weren't already connected, then they should be connected, and unioned within their respective disjoint sets
- `find-set` and `union` are both disjoint set operations, where find-set finds the disjoint set a given node belongs to
- so for instance, `find-set(u) != find-set(v)` will check the disjoint sets that each node belongs to, and if they're in different sets then it means ==they aren't connected at the moment==
- `make-set` will just create a new set whose only member is the given node
```
  procedure make-set(x)
	  x.p = x // x is its own parent
	  x.rank = 0 // an upper bound on the number of edges in the longest path in set, used for union operation (smaller ranks points to root of larger rank)
```

### complexity

- the complexity of kruskals mainly depends on the implementation of the disjoint set structure
- using path compression and union by rank, the complexity is $O(|E| log|V|)$