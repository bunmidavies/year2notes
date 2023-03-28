[[COMP26020]]

### background + initial requirements
- as covered within [[intro to linear programming]], it can be seen that its possible to represent maximisation/minimisation problems on a graph using lines
- it should be noted that in order for the simplex algorithm to work, all the angles formed by different constraints are ==less than 180 degrees== in the feasible region, i.e. no two constraints are pointing into the region:
![ | 550](https://i.imgur.com/pk7MB7m.png)
- these constraints form a ==concave shape== within the graph
- the simplex algorithm is also applied differently according to whether the ==origin== is in the feasible region or not
- as well as this, only linear programs where $b\geq 0$ are discussed - this means an initial feasible solution of $0$ exists - an initial feasible is required for the simplex algorithm

### slack variables
- slack variables are used to get rid of any 'space' within certain constraints, e.g.
- $-x_1 + x_2 \leq 11$ means that 11,10,9... are all acceptable -> $-x_1 + x_2 + s_1 = 11$, where $s_1$ is the slack variable
- there are two main requirements for ==slack form==:
	1. when all the constraints (other than non-negativity) are equalities
	2. every variable only appears in a single equation, and has a coefficient of 1