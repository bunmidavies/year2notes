[[COMP26120]]

### formal description of linear programming problems

- formally, a linear programming problem is an ==optimisation problem== which can be represented using a set of linear relationships - we are trying to minimise or maximise something, given a set of constraints
- a linear relationship takes the form $a_1x_1 + ... a_nx_n \leq ...$
- these constraints are inequalities rather than just equations
- all the variables within these equations must be greater than or equal to zero

### visualising linear programming problems as graphs
- taken as an example from the lectures, there is a farmer trying to maximise the amount of profit from a field where they can plant barley and wheat
- the following variables can be represented as such:
	- seeds of barley planted: $x_b$
	- money gained per kg of barley sold: $S_b$
	- seeds of wheat planted: $x_w$
	- money gained per kg of wheat sold: $S_w$
- therefore the problem can be represented as a linear programming problem: maximising $S_bx_b + S_wx_w$
	- $x_b + x_w \leq A$ (number of seeds cant exceed area available)
	- $F_bx_b + F_wx_w \leq F$ (certain amount of fertiliser for barley/wheat * no of seeds of each planted is constrained)
	- $P_bx_b + P_wx_w \leq P$ (same constraint idea as fertiliser, except for pesticide)
	- $x_b,x_w \geq 0$ (cant plant negative number of seeds)
- any variables (other than seeds planted) can have values plugged in, and this problem can then be visualised with a graph, with lines representing certain constraints
- ==the optimal solution will always lie at a vertex of lines in this graph== (a vertex being a point where the lines cross)

### converting to a linear programming problem in standard form
- in order for a linear programming problem to be in standard form:
	- all equations (which aren't non-negativity) must be ==inequalities==, not equalities - to convert an equality, turn it into two inequalities
	- all inequalities should use $\leq$, never $\geq$ (unless non-negativity obviously) - to fix any inequalities you must invert them so the sign direction flips 
	- the problem should always be to ==maximise==, therefore an equation which youre trying to minimise should also just be inverted so that it now needs to be maximised

### representing problems as matrices
- a helpful step for converting from linear to matrix is firstly to make sure all the variables are in the same order, for instance:
![](https://i.imgur.com/cuGjGOX.png)
- the form we're trying to create is:
	- Maximise: $c^Tx$
	- Subject to: $Ax \leq b$, $x\geq 0$
- where $A$, $x$, $b$ and $c$ are all matrices (a vector also counts as a matrix, as $x$ and $b$ are vectors)
![](https://i.imgur.com/Q3lzVQo.png)
