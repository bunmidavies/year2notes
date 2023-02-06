[[COMP26120]]

graphs should have the following operations
- `EMPTY` returns the empty graph
- `ADDEDGE`, `REMOVE EDGE`, `ISEDGE` all operate on $(u,v)$, i.e. a given node and edge
- `SUCCS` returns the successors of a node

==Adjacency Lists== are the most common method of representing graphs - it involves storing a list / set of successors for each node

The memory involved in an adjacency list is $O(|V| + |E|)$

the complexities for the graph operations on adjacency lists are as follows:

| operation       | implementation           | complexity |     |     |     |     |
| --------------- | ------------------------ | ---------- | --- | --- | --- | --- |
| addedge(u,v)    | append v to succs(u)     | $O(1)$     |     |     |     |     |
| removeedge(u,v) | remove v from succs(u)   | $O(        \| V   \| )$  |     |     |
| isedge(u,v)     | search for v in succs(u) | $O(\| V   \| )$  |     |     |
| succs(u)        | return succs(u)          | $O(1)$           |     |     |     |     |

***

==Adjacency Matrices== are simply a big truth table, where the following holds in the matrix:
- *m(u,v) = TRUE iff edge from u to v*
this means you have to store $|V| \times |V|$ to map to booleans, meaning the memory complexity for this representation is $O(|V|^2)$, meaning this method is bad for ==sparse graphs== (graphs with very few edges)

the ==advantage to an adjacency matrix== is that the complexities of graph operations are nearly all constant

| operation       | implementation           | complexity |     |     |     |     |
| --------------- | ------------------------ | ---------- | --- | --- | --- | --- |
| addedge(u,v)    | append v to succs(u)     | $O(1)$     |     |     |     |     |
| removeedge(u,v) | remove v from succs(u)   | $O(1)$  |     |     |
| isedge(u,v)     | search for v in succs(u) | $O(1)$  |     |     |
| succs(u)        | return succs(u)          | $O(\|V\|)$           |     |     |     |     |


To decide how to represent a graph, the following should be considered:
- How dense is the graph?
- What operations will be performed on the graph?