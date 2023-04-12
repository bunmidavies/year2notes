[[COMP21111]]

- We use conjunctive normal form in order to be able to use more efficient satisfiability algorithms
- One of the most efficient algorithms is **DPLL**

## DPLL on QBFs

- We say that a QBF is in [[CNF]] if its either $\top$, $\bot$, or in rectified prenex form, taking the form:
$$[q]_1 p_1 ... [q]_n p_n(C_1\land ... \land C_m)$$
- where $[q]$ is a quantifier, and $C_1...C_m$ are propositional clauses
- Example:
  $$\forall p \exists q \exists s((\neg p \lor s \lor q) \land (s \lor \neg q) \land \neg s)$$
- So the process to getting to a suitable form for DPLL with QBFs is:
	- Rectification ([[QBF - rectification]])
	- Prenexing ([[prenex form]])
	- Propositional [[CNF]] rules

- DPLL takes inputs:
	- $Q$: the quantifier sequence ($[q]_1 p_1 ... [q]_n p_n$)
	- $S$: the set of clauses ($C_1\land ... C_m$)
- DPLL will return whether $Q$ over $S$ returns true or false, by using [[splitting for QBFs]], and [[unit propagation]]

- DPLL algorithm
![](https://i.imgur.com/GrvtoFW.png)


- with the `case` statement towards the bottom, this is where we branch off
- the $S \cup \{L\}$ is used to indicate that $L$ is added as a unit clause to $S$