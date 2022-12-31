[[COMP24011]]

The first thing to understand is that alpha beta pruning can be added to the already existing minmax algorithm, and ==does not change the outcome== of the algorithm. It simply exists to speed up the process, and skip nodes which will not affect the outcome of the algorithm

How alpha beta pruning actually works can be seen as moving on from a node as soon as it's known that no further nodes will affect the algorithms result. This works through:

it is applied to the [[minimax algorithm]]

==at a maximising node==, $\beta$ comes from the parent, and $\alpha$ is the highest-value child so far

==at a minimising node==, $\alpha$ comes from the parent, and $\beta$ is the lowest-value child so far

==**when to stop processing**==
for alpha-beta pruning, you stop processing the current node once $\alpha \geq \beta$
