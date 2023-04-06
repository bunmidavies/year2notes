[[COMP26120]]

### ~ background + initial requirements
- as covered within [[intro to linear programming]], it can be seen that its possible to represent maximisation/minimisation problems on a graph using lines
- it should be noted that in order for the simplex algorithm to work, all the angles formed by different constraints are ==less than 180 degrees== in the feasible region, i.e. no two constraints are pointing into the region:
![ | 550](https://i.imgur.com/pk7MB7m.png)
- these constraints form a ==concave shape== within the graph
- the simplex algorithm is also applied differently according to whether the ==origin== is in the feasible region or not
- as well as this, only linear programs where $b\geq 0$ are discussed - this means an initial feasible solution of $0$ exists - an initial feasible is required for the simplex algorithm

### ~ slack variables + slack form
- slack variables are used to get rid of any 'space' within certain constraints, e.g.
- $-x_1 + x_2 \leq 11$ means that 11,10,9... are all acceptable -> $-x_1 + x_2 + s_1 = 11$, where $s_1$ is the slack variable
- there are two main requirements for ==slack form==:
	1. when all the constraints (other than non-negativity) are ==equalities==
	2. in each equation there is a variable that only appears in that equation, and has a coefficient of 1
- if you have a list of equations following these rules, then you can say that you have a linear programming problem in slack form
- if the variables that appear in more than 1 equation are set to 0, its possible to read off a ==possible, but not neccesarily optimal== solution to the given linear programming problem in slack form

### ~ basic variables, non-basic variables + pivoting
- following on from slack form above:
	- ==basic variable== = a variable that only appears in one equation
	- ==non-basic variable== = a variable that appears in more than one equation
- thus we can say: ==basic solution== = a solution where all non-basic variables are 0
- ==pivoting== = swapping a basic and non basic variable, i.e. the basic variable is now non basic, while the non-basic variable is now basic

### ~ simplex example
- taking the example from above, the equations have been converted to ==slack form==, then represented as an ==augmented matrix== (to make the problem at hand clearer)
- in the example, $x_2$ (the non basic variable) gets swapped with $s_1$ (the basic variable) - in the video $x_2$ is selected due to having the largest negative coefficient, and $s_1$ is selected as it has the least slack. ==This swapping process is pivoting==
![](https://i.imgur.com/FYWg1uE.png)
- to represent this swap, we create a new augmented matrix by making $x_2$ appear only once in an equation with a coefficient of 1
![](https://i.imgur.com/Ned0O0i.png)
- from this point on, the simplex algorithm is just pivoting until an optimal solution is reached
- ==an optimal solution is where there are no negative coefficients in the final equation==
- in this new pivot, we pick $x_1$ to be swapped with $s_3$, as $x_1$ is the only negative coefficient left, and $s_3$ has the most slack (ignoring negative slack)
- we want to make the row with $s_3$ have its $x_1 = 1$, so we divide the row, and subtract from other rows to make $x_1 = 0$
![](https://i.imgur.com/A6nZtgv.png)
- another pivot needs to be performed, since there is now a negative coefficient for $s_1$ - we calculate that $s_2$ has the least slack, thus we are now swapping $s_1$ and $s_2$
![](https://i.imgur.com/RUkm9Wm.png)
- in this new basic solution, $x_1 = 12$ and $x_2 = 15$ (reading off the right column in the bottom matrix), giving the optimal solution of 132
![](https://i.imgur.com/hqP4Y31.png)
