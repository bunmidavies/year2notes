[[COMP21111]]

- pure literal rule is a [[DPLL - QBFs and Propositional]] optimisation

## propositional logic
- **Pure literal elimination**
- This rule is similar to the pure atom rule used for satisfiability - if an atom only occurs without any negation, we know that its polarity is the same everywhere, so we can replace it with $\top$ or $\bot$
- A literal $L$ in a formula $F$ is known as **pure** iff:
	- $F$ contains no clauses of the form $\bar{L} \lor C$ (no clauses containing complement of $L$)
- If we find a **pure** literal within any clause, we can remove **all clauses which contain this literal**. This also doesn't affect satisfiability
- Certain literals may also become pure during the process, as you may remove certain clauses while eliminating some pure literal, which happens to remove a certain clause which was causing another literal to be impure

## quantified boolean logic
- Let $Q$ be a quantifier prefix and $S$ a set of clauses
- let literal $L$ be pure in $S$ then $\neg L$ doesn't occur in $S$
- **If $L$ is existentially ($\exists$) quantified in $Q$ then all clauses in which $L$ occurs are removed**
- **If $L$ is universally ($\forall$) quantified in $Q$ then we can remove $L$ from all clauses in which $L$ occurs (not the whole clause)**

- *universal literal deletion*
	- given a non tautological clause $S$ - if there is a universally quantified variable $p$, and all existentially quantified variables in $S$ are quantified before $p$, $p$ can be removed without affecting the truth table of $S$
![](https://i.imgur.com/YKQANcH.png)
