[[r+n.pdf#page=150]]
# Week 1 topics
- Inferential tasks, being solved using search algorithms (DFS, BFS, Branch-and-bound, A*)


<u>part 1 of video 1</u>
- Inferential task example
  Placing objects within a house, and moving throughout the house
- Atomic propositions denoting the current situation of a problem can be called **fluents** (as they're subject to change)
- Goals of a problem can typically be a number of fluents we just want to be true
- Actions can simply store what preconditions are required, and which fluents are affected by such an action. (Fluents can be changed by basically deleting old fluents, and adding new fluents)

- **Such problems can be represented with trees - nodes represent a situation, and edges represent certain decisions which are made**
- These trees can also be better viewed as directed / undirected graphs (although trees are just a type of graph)

***
### Heuristics
- The rules which a program **has to obey** to search through a space of possible inference (situations) in order to find a specific inference (situation)
- [[Heuristic Methods]]
***

<u>part 2 of video 1</u>

- Inference rules are also known as **syllogisms**, Aristotle identified all valid syllogisms.
- Syllogisms are the arguments, while syllogistic is the language
- The question is whether there is a process to break down propositions
- In logic, **There exists... = Some... = $\exists$**


- Inference rules define a tree of knowledge states, such that proving a conclusion can basically be done by searching a tree


<u>video 2</u>

- dude goes over bfs and dfs but i genuinely find it more confusing since he uses the word Queue to refer to everything even though thats not what he actually means
- The main difference within his explanation (which does kind of make sense) is that within a bfs you would add daughters from the current node to the **end of the queue**, which with DFS you would add daughters to the **front of the queue** (but like all at the same time such that the leftmost node is always ending up at the front of the queue no?)
- DFS = branch by branch
- BFS = row by row

- we will often want to find the **least cost** solution whenever we're looking for a solution. We'll typically assume that each action has a non-negative cost, so at each node there is a cost-so-far
- there will typically be lower bounds to reach x node from the current node, and these can be determined using either:
	- branch-and-bound
	- A*
- $K(u) = C(u) + U(v)$ for any node $v)
  This basically means the cost of getting to $u$ from $v$ is the cost of getting to $u$ + the minimum cost of getting to $v$ (our current point)
- If $\mu$ is a goal node and $K(\mu) \leq K(v)$, then abandon v, because if every node has a non negative cost, there isn't any chance of finding a better path to a goal node **when the cost of just reaching $v$ is already greater than or equal to the cost to reach $\mu$**

***
***
Basic pseudocode for branch-and-bound:
```
bestcost = Integer.MIN_VALUE

bnb(queue,bestcost)
	if !queue.isEmpty()
		firstnode = pop first element from queue
		if K(firstnode) < bestcost
			if firstnode is a goal node
				currentbest = firstnode
				bestcost = K(currentbest)
			else
				add daughters of firstnode to front of queue
		bnb(queue,bestcost)
	else if bestcost != Integer.MIN_VALUE
		return currentbest
	return false
```
Note again that he treats the queue like you can add x daughters to it, and that they'll be going from left to right in the correct order within the queue (when in reality you'd probably have to adjust this a little)
***
A* is comparatively simpler, because it can essentially be presented like a BFS
```
ast(Queue)
	if !queue.isEmpty()
		firstnode = pop from queue
		if firstnode is goal node:
			return firstnode
		compute daughters of firstnode and add to queue
		order queue by cost //or use priority queue
		return ast(queue)
	return false
```
The key to A* is using a Priority Queue or any kind of queue which is able to order itself, such that the closest daughter/entire path is ALWAYS being explored first
Note that $K$ *is the cost to reach daughter node + cost to reach current node*
***

## 3.3 (R + N) - searching for solutions
- Search cost = time taken by search to find goal node
- Total cost = length / cost of the actual path which reaches goal node


## 3.5 (R + N) - informed search strategies
- Informed search strategy means - a strategy which uses problem specific knowledge beyond the definition of the problem to find solutions more efficiently than uninformed strategies