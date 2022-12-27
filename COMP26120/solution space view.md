[[COMP26120]]

the ==solution space view== is one of the main paradigms for [[algorithmic techniques]] - it involves exploring all possible solutions, and selecting the ones which are valid solutions

when we explore all possible solutions to a problem this is known as ==brute-force== 

if we generate the set of solutions incrementally then search this set, we call this ==enumeration== - its a type of brute-force, but we are aware of some structure of the solution space

enumeration is typically involved when the solution space is found to have a ==tree structure==. Therefore, problem solving can be done as a ==search== of the tree

if there are $n$ solutions, the complexity of brute-force/enumeration is $O(n)$ - this usually results in $O(n^2)$ complexity where $n$ is the input

==pruning== is the typical way to improve the efficiency of searching a tree. With a brute force technique, this is better known as ==depth-first-search + pruning==
pruning is used in different ways for branch-and-bound/backtracking
- in ==backtracking== a branch is pruned if it cant be extended to any solution
- in ==branch-and-bound== a branch is pruned if it cant produce an already known solution which is *better*

the ==SAT== algorithm is a common example of where backtracking is used, and ==MAX-SAT== algorithm is a common example of where branch-and-bound is used

[[greedy algorithms]] are a type of solution space view technique, which will always pick the ==best local choice==