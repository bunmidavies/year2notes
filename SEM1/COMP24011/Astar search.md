[[COMP24011]]

[[basic search]]

the A* search is the most widely known form of a ==best-first-search==, an ==informed== type of search

A* evaluates nodes by combining the cost to reach the node with the ==estimated== cost to get from the node to the goal, from a heuristic function
$$f(n) = g(n) + h(n)$$

the requirement for the heuristic function $h(n)$ is that it is ==never an overestimate== - the word for this is [[admissible]]

==steps in the A* search==
at the current node, all the children nodes are added to a ==priority queue==

the node with the lowest $g(n) + h(n)$ (i.e. the cost to reach that node, + the estimate from that node to the goal) will be at the front of the ==priority queue== - this node is popped

for A* to be used within ==graph searches==, the heuristic function also has to be ==consistent== - this means that given some node $a$, and its child $b$, $f(n)$ from $a$ shouldn't be more than the cost to get to $b$, plus $h(n)$ from $b$ (this logically makes sense with the word 'consistent')

A* is not suitable for many ==large scale problems== as it needs to store all generated nodes in memory