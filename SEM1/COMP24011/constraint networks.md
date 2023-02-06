[[COMP24011]]

A **constraint network** is a tuple:
	$$\langle\bar{x},\bar{D},\mathcal{C}\rangle$$

- $\bar{x}$ = $x_1,...,x_2$ = set of variables
- $\bar{D} = D_1,...D_n$ = set of domains, one for each variable
- $\mathcal(C) = {R_1,...,R_m}$ = set of relations (==constraints==)

- $x_i$ can only take on the values within $D_i$. Therefore we say $D_i$ is the ==domain== of $x_i$
- ==arity== of a relation = number of arguments
- $R_j$ is a relation with $j$ arguments (arity of $j$) over the domain:
  $D_{i_{j,1}} \times ... \times D_{i_{j,a(j)}}$
${i_{j,1}}$ to ${i_{j,a(j)}}$ are indices from $1,...,n$

- The basic point of $R_j$ is to place constraints on what can be assigned the the variables
- whichever pairs that are ==not== in $R$, are the ==constraints== i.e. values which are impossible to assign
- A solution is a tuple (i.e. a variable assignment) which satisfies all the contraints of all $R_j$, and only contains variables which are allowed:

  $\bar{a} = a_1,...,a_n$ such that
  - $a_i \in D_i (1 \leq i \leq n)$
  - $\langle a_{i_{j,1}},...,a_{i_{j,1}} \rangle \in R_j (1 \leq j \leq m)$

