[[COMP24011]] - [[constraint propagation]]

[[arc-consistency]] can be known as 2-consistency
[[path-consistency]] can be known as 3-consistency

k-consistency is just a way to ==generalise consistency== over some arbitrary number of variables - however the algorithm for establishing this gets tricky, being exponential in time and space in terms of $k$

a network is directionally k-consistent ($k \geq 4$) if for any ordered sequence of $k$ variables, and any assignment to these variables without violating any constraints, there exists a value in the $k$th domain which ==doesn't violate== any previous constraints in the sequence of $k$ variables

a network is ==strongly== directionally k-consistent if it is directionally j-consistent for all $j\leq k$ (i.e. it isnt only directionally k-consistent, but directionally consistent for all values ==leading up to k==)