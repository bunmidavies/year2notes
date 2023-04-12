[[COMP21111]]

- tableaux for plfd takes a similar form to [[tableaux for prop logic]]

- tableaux works on signed formulas - an expression $A = b$ where $A$ is a formula and $b$ is a boolean value
- $A = b$ is true in interpretation $I$, if $I(A) = b$
- $A$ is satisfiable if and only if  the signed formula $A =1$ is satisfiable

- atomic formulas $x = a$ is replaced with $x \in \{a\}$ 
- $(x \in D)  = 1$ is the same as $x \in D$
- $(x \in D) = 0$ is the same as $x \notin D$ 

## plfd tableau rules

[[tableaux rules]]
![](https://i.imgur.com/wMdTHT6.png)


## building a tableau

- a branch + formula is chosen
- rules are applied in order to expand tableau

- a branch is **closed** if it contains $x \in \{\}$
- a branch is **open** otherwise

- a tableau terminates if:
	- all branches are closed - formula is **unsatifsiable**
	- all rules have been applied and the branch is open - formula is **satisfiable**

- a tableau is valid if $A = 0$ only contains closed branches. This means that $A = 0$ is unsatisfiable, therefore a **tautology/valid**

## [[plfd tableau example]]