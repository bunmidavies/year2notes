[[COMP24011]] / #comp24011 

as part of the [[planning]] section

a ==literal== is a fluent, or the negation of a fluent

a ==planning graph== consists of levels of ==situations==, and levels of ==actions== which can be taken from specific situations - they provide suitable underestimates which are ==crucial== for [[searching algorithms]] (A* / branch-and-bound)

there is a level $S_0$ for the initial state, consisting of the nodes (fluents) which hold in $S_0$. Then there is $A_0$, consisting of nodes which might be applicable for each possible action in $S_0$. This repeats until a termination condition is reached

this means $S_i$ holds ==all the literals that *could* hold at i==

the planning graph cannot answer the question a planning problem asks, but can ==estimate== how many steps are needed to reach the goal state:
- the smallest $i$ such that $g \in S_i$ is a good underestimate for the number of steps required to reach a ==specific goal predicate==
- the max value associated with any $g \in G$ is a good underestimate for the number of steps required to reach the ==set of goals==

within a planning graph, there are ==persistence actions== also called *no-op*s. This is where no action has negated a literal, so basically nothing has happened. In R+N this is shown as a small white box $\square$ 

determining [[mutex links]] can be difficult

A planning graph is ==polynomial== in the size of the planning problem. For a problem with $l$ literals and $a$ actions, each ==situation== has no more than:
- $l$ nodes
- $l^2$ mutex links
each ==action== has no more than:
- $a + l$ nodes
- $(a + l)^2$ mutex links
this means, the time and space complexity of building a graph with $n$ levels is $O(n(a+l)^2)$