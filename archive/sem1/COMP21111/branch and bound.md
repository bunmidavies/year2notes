[[COMP24011]]

$K(v) = C(v) + U(v)$ where $v$ is the current node
and:
- $C$ = cost-so-far
- $U$ = underestimate of achieving goal from given node

The basic points of branch and bound are to use a ==queue== to store nodes which are to be explored. The algorithm only ends once the ==queue is empty==

The first node $v$ from the queue is taken, and $K(v)$ is compared to the current best

If $K(v)$ is ==already greater or equal to current best==, we know that we cannot encounter negative costs, so we will not find a better solution down this path. None of its daughters will be added to the queue, and you move to the next element in the queue

If $K(v)$ is ==less than the current best==, we check if $v$ is a goal node. If this is the case, we have found a cost to reach a goal node which is less than our current best, so we ==update current best== - the new current best is $K(v)$

If $K(v)$ is ==less than the current best but not a goal node==, we still have to explore more. This means we add all of $v$'s children nodes to the front of our queue, and continue with the algorithm

==Slide from the lecture:==
![Uploading file...kmi7l]()
