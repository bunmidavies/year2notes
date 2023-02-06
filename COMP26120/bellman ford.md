[[COMP26120]]

==|V| = number of vertices==

in a weighted graph, a weight matrix $w$ is used, and works like an adjacency matrix for directed graphs, where $w(u,v)$ means the edge between $u$ and $v$ has weight $d$

if $w(u,v) = \infty$, then there is ==no edge between u and v== - this also means if a path has a weight of $\infty$, then the path is not feasible/doesnt exist

$\delta(u,v)$ represents the distance between $u$ and $v$

==Bellman Ford computes the shortest paths from start node s to any node==

it starts by over-estimating the distance between any two nodes, i.e. setting all distances to $\infty$ - we then ==relax== certain edges i.e. find out if there is any way to find a better edge than what we currently have

```
bellmanford(s)
	D <- initEstimate(s)
	for i = 0 ... |V| - 1 do
		for all (u,v) where w(u,v) != inf do
			relax(u,v)
	return D

initEstimate(s)
	D(u) <- inf for all u
	D(s) <- 0 //start node obvs has distance 0 from itself
	return D

relax(u,v)
	if D(u) + w(u,v) < D(v) then
		D(v) <- D(u) + w(u,v) //update distance if it is better
```

when iterating over all edges a->b in the main algorithm, we check if we can get to b quicker than previously, and if so update the estimation on b
this repeats up to |V|-1 times

the bellman ford algorithm terminates once none of the edges are updated in a singular run

## correctness + complexity

the correctness of bellman ford is demonstrated using a [[loop invariant]]

in round I:
- estimated shortest paths up to length I are ==precise==
- $\forall u \in V . D(u) \geq \delta(u)$
Therefore, at the end of round 0, D is precise up to length 0
We assume that at the end of round i, D is precise up to length i

We need to show that at the end of round i + 1, D is precise up to length i + 1:
- Prefix of a shortest path is also a shortest path
- Assume path "s -> P -> u -> v" is a shortest path of length i + 1
- Therefore "s -> P -> u" is the shorest path of length i, and we already know that D(u) is precise
- Round i + 1 relaxes the edge (u,v), so now D(v) is precise after round i + 1

- in the ==worst case==, we do |V| rounds of bellman ford
- each round inspects |E| edges, and the time for relaxing an edge is O(1)
- therefore, the complexity of bellman ford is ==O(|V||E|)==

## negative weight cycles

bellman ford can detect where negative weight cycles occur:
- iterate until D does not change
- ==if D still changed in the |V|th round:== report negative cycle