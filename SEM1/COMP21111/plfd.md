[[COMP21111]]

## plfd

- PLFD is a family of logics - each instance of PLFD has:
	- set $X$ of variables
	- a mapping $dom$, so for every $x \in X$, $dom(x)$ returns a **non-empty finite** set (the **domain** for $x$)

- following from the microwave example, $dom(door) = \{open,closed\}$

## plfd formula

- if $x$ is a variable and $v$ is a value in the domain of $x$ ($v \in dom(x)$), $x = v$ is an **atomic formula**
- other formulas are built from **atomic formulas** like [[propositional logic]], using the same connectives
- example: mode = cooking $\rightarrow$ door = closed $\land$ $\neg$user = nobody

## plfd semantics

- interpretation $I$ is a mapping for values from $X$ (variables) to $dom(x)$, where $x \in X$

- $I(x = v) = 1$ if and only if $I(x) = v$
- past atomic formulas, plfd is the same as propositional logic

- in order for a formula to be a **tautology (valid)**, it is important that the formula covers the domain of any involved variables:
![](https://i.imgur.com/RPKapHk.png)


- [[tableaux for plfd]] covers how to determine satisfiability for plfd without converting to logic ([[plfd to prop logic]])