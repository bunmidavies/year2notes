[[COMP21111]]
[[LTL]]

- all possible behaviours of a transition system can be defined through a computation tree

- given $\mathbb{S}$ is a transition system, and $s$ is a state, the computation tree for $\mathbb{S}$ starting at $s$ is a possibly infinite tree
- nodes of the tree are states (existing within the transition system)
- the root of the tree is $s$
- for each node $s'$ in the tree, all children are nodes $s''$ such that $(s',s'')$ is a pair in the transition system's relations

- a computation path is a sequence of nodes that follow eachother, and if finite it must be the **maximal sequence**

![](https://i.imgur.com/rOFotf7.png)


- computation trees can be infinite