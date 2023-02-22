[[COMP26120]]

- A ==cut== of an ==undirected== graph is a partition of the nodes in the graph, $V$
- essentially, you have $S$ which are the nodes removed in the cut, and the cut itself, $V - S$

- A cut ==respects== some set of edges $A$ if no edge in $A$ 'crosses' the cut
- ==An edge is 'crossing' the cut== if one endpoint is in $S$, and the other is in $V - S$ 
- If this edge is crossing the cut, then it is a ==light edge== if the edge's weight is the ==minimum== out of all edges which cross the cut (*Multiple light edges can exist if multiple are the minimum*)

### Trainline example
![](https://i.imgur.com/QSVPIvq.png)
- In this example, the cut is clearly visible - this makes Karlsruhe and Munish the $S$ as explained above - so in this case, $V - S$ = Germany - {Karlsuhe, Munich}
- The routes which cross the cut include Bonn -> Karlsruhe, Bonn -> Munich, ? -> Karlsruhe and ? -> Munich
- Therefore, the edge which crosses the cut and has the minimum weight is Bonn -> Karlsruhe, meaning this is the ==light edge== (highlighted in gold)
- We can then take any set of edges, and check if the cut respects them. For instance Frankfurt -> Hamburg, Hamburg -> Berlin and Frankfurt -> Bonn ==respect the cut== because none of these cross