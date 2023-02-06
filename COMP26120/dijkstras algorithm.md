[[COMP26120]]

dijkstras algorithm provides the shortest path in a graph from nodes a to b

```
dijkstra(s):
	F = emptyset
	D = initestimate(s)

	while D is not empty:
		u = D.pop()
		F.add(u)
		for each neighbour of u which isnt in F:
			D.add(v)
		relax(u)

relax(u):
	for each neighbour v:
		if D(u) + weight(u,v) < D(v):
			D(v) = D(u) + weight(u,v) //better weight found
			P(v) = u //set predecessor of v
```

the difference between [[bellman ford]] and dijkstra is that `D` in the pseudocode above is a ==priority queue== ordered by distance, meaning the shortest node will always be popped first

we use a minHeap in dijkstras - by adding nodes as they're discovered into the priority queue, this means that we wont end up ever exploring nodes which are unreachable - so ==all nodes dont need to be labelled with infinity to start==

### complexity
- every edge is relaxed ==at most once==
- every node is added and removed from PQ ==at most once==
- cost of relaxing/addition/extraction in a min heap is $O(log|V|)$ where |V| is still no of vertices in the graph
- therefore overall complexity of dijkstras is $O((|E| + |V|)log(|V|))$