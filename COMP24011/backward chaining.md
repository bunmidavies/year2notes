[[COMP24011]]

it can be better to think of planning as starting off with a set of goal predicates, and ==working backwards== to achieve starting predicates

for instance, if we alter some set of goal predicates, we can say in order to reach our original set of goals, we just have to reach this new set of goals we've created - we have chained backwards in this case

with backward chaining we can create another ==tree==:
- each node represents a ==list of goals== - $goals(v)$

- the ==root== of the tree represents the goals ==to be achieved==

- the possible moves at node $v$ are actions $\alpha$ such that:
	- add-list($\alpha$)$\cap$goals($v$) $\neq \emptyset$ 
	- del-list($\alpha$)$\cap$ goals($v$) $=\emptyset$ 
(these basically mean that any action should be the *last* action to achieve the goals in the node - if the action were to delete some of the goals, then it wouldn't be a valid action to reach the node)

- the daughter of any node $v$ represents (goals$(v)$ $\setminus$ add-list($\alpha$) $\cup$ preconds($\alpha$)) - computing this node is called ==regressing== $\alpha$ through $G$

- a node $v$ is a ==success node== if $goals(v)\subseteq$ initial situation - i.e. if we've gotten to a point where all the required goals are actually already achieved by our starting state in the problem (==NOT== the root of the tree, the actual initial situation)