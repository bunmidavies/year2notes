[[COMP26120]]

intro to graphs synchronous summary session

a ==directed graph== is a set of nodes $V$ and edges $E$, where $E \subseteq V \times V$
in the case of a directed graph, the first element in each pair of $E$ is the ==from==, while the second is the ==to==

in an undirected graphs the edge pairs aren't ordered, so the above about $E$ doesn't apply

a ==path== is a sequence of nodes $u_1...u_n$ where $\forall i \in \{1 .. n - 1\}.$ - a path by default ==does not have cycles== i.e. a path with the same start and end node

==simple graphs== have two main attributes:
- no parallel edges (two edges with same origin and destination)
- no self-loops

==spanning subgraph== - a subgraph which contains all nodes from its previous parent graph (just not all edges)

[[representing graphs + graph operations]]
[[graph traversal]]
[[toppological sort]]