[[COMP24011]] / #comp24011 

==a planning problem asks if we can reach a goal state from an initial state==

we apply search algorithms to find ==minimum cost plans==

when planning, we need a ==cost model== for actions
$$C(carry(x,y,z))=2$$

the cost to ==reach a node== $v$, within some ==search tree== is defined as:
$$C(v) = \sum{\{C(\alpha)|actions(v)\}}$$

where $actions(v)$ are the actions which reach $v$

an ==underestimate== of the cost to reach a goal $G$ is required:
$$U(v) = |G \setminus situation(v)|$$

[[planning graphs]] are a better way to obtain solutions without needing for blind searching like ==A*== or ==branch and bound==

#### a classic type of planning problem is ==The blocks world==
the domain consists of a set of cube-shaped blocks sitting on a table
blocks can be stacked, but only one block can fit directly on top of another
a robot arm can pick up and move blocks, but only ==one block at a time==
the goal is defined with first order logic as $Goal()$

#### a hybrid approach to planning is [[means-ends-analysis]]
