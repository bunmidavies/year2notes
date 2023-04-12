[[COMP24011]]

constraint propagation also known as ==forward jumping==, is a method of solving [[constraint satisfaction problems]]

there are 3 covered forms of constraint propagation:
- [[arc-consistency]]
after creating a graph to represent the constraint network, we can traverse the graph without the need to ==backtrack==, due to arc-consistency. Arc-consistency makes the ability to search through a constraint network easier, and more efficient

- [[path-consistency]]

- [[k-consistency]]

if a constraint network is ==strongly k-consistent==, then it must have a ==solution== 

however, the downside of k-consistency is that enforcing it is ==computationally expensive== (time complexity becomes exponential with respsect to $k$)


==assumptions==
![](https://i.imgur.com/drENYHf.png)

