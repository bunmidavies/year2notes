[[COMP21111]]

OBDDs are the same as [[BDD]]s, but also:
- introduce an ordering $>$, which makes the tests ==in order==

==Every boolean function has a unique OBDD==
We can describe OBDDs are being ==canonical== for boolean functions

boolean operations become ==easy to implement== with OBDDs - [[boolean operations with OBDDs]]

## building an obdd with `integrate` and `obdd`

- `integrate` is the main algorithm used in order to add nodes to an obdd
- `obdd` is then the overall algorithm which is used to create an obdd based off some given propositional formula

## integrate
![](https://i.imgur.com/vqEi9oL.png)

- integrate will return the node if it already exists in an obdd, or create it otherwise
- integrate also checks **if the left and right nodes are the same** - if this is the case, then $n_1$ i.e. the left node can just be returned on its own - this **eliminates redundancies**

## build obdd
![](https://i.imgur.com/PEMyekj.png)

- the obdd procedure combines the algorithm for building decision trees, with the algorithm for eliminating redundancies 

note that the `p = max_variable(F)` in order to ensure the ==correct ordering== is followed

- So given some propositional formula, the basic steps are:
	- Simplify the formula
	- If it is simply $\top$ / $\bot$, then return $1$ / $0$ node
	- Otherwise, pick the variable with the highest order. Using this variable:
		- Replace it with $\bot$ and generate the obdd for that new formula
		- Replace it with $\top$ instead and generate the obdd for that new formula
	- Once you've got the obdds from these two operations, use `integrate` to generate the entire obdd

## example 

we want to integrate the following into an existing dag
$$((q\rightarrow p)\land r \rightarrow (p\leftrightarrow r)\land q)$$
given the ordering $p > q > r$
this is the existing dag
![](https://i.imgur.com/I5fDOt1.png)


- the formula is already simplified, so now we just pick the max variable - $p$
- we obtain $n_1$ and $n_2$ (by replacing $p$ with $\top$ and $\bot$ respectively)
	- $(\top \land \top \land q)$, so just $q$ - therefore we call obdd again:
		- replacing $q$ with $\top$ returns $\top$
		- replacing $q$ with $\bot$ returns $\bot$
	- $\neg q \land \neg r \land q$, therefore $\bot$ (contradication with $\neg q$ and $q$)
- so it looks like we will call integrate($q$,$p$,$\bot$,$D$)

