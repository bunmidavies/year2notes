[[COMP21111]]

A binary decision diagram / BDD is a ==dag== (directed acyclic graph) built like a binary decision tree but containing:
- ==no redundant tests==
- ==no isomorphic subtrees==

BDDs cant be considered trees because you can have multiple nodes directed to ==the same node==, e.g.

BDDs have properties which make them useful:
- Satisfiability checking can be done in ==constant time==
  this can be done by checking if the graph is a $0$ on its own
- Validity checking can be done in ==constant time==
  this can be done by checking if the graph is a $1$ on its own

However, ==equivalence checking== and ==some boolean operations== still aren't simple for BDDs

The main reason for this is because the ==ordering== within BDDs can be arbitrary, and when trying to split on specific variables in the diagram, different ordering can make this task difficult - in short, ==diff. branches of the dag are made in diff. orders==

[[OBDD]]s overcome these limitations