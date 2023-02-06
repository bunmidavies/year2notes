[[COMP26120]]

a topological sort is applicable when we have:
- a set of tasks (e.g. a build sequence when developing software) which have certain ==dependencies==
- this means for certain tasks, they may require other tasks to be completed first

this means these tasks can be represented as a ==directed graph==, and a build sequence i.e. some path can be found

to achieve topological sorting, a ==Directed Acyclic Graph== is used (no cycles is important to achieve topological sorting)
all nodes then need to be arranged sequentially, such that all edges point 'forwards' - then a DFS based algorithm can be used to generate a topological ordering but also detect any cycles
once a node has no edges to new nodes, it can be added to a ==done list==

when an 'open' node appears in the list of neighbours for a given node, this means a cycle has been detected (so an error can be returned at this point for any task + dependency type problem)