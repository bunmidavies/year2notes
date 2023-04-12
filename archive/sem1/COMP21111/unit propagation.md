[[COMP21111]]



## unit propagation for QBFs
- $Q$ = quantifier sequence
- $S$ = set of clauses

- if $S$ contains a unit clause ($p$ or $\neg p$), then:
	- If $Q$ contains $\exists p$ or $p$ doesn't occur in $Q$:
		- remove every clause containing the literal $L$
		- replace every clause of the form $\neg L \lor C$ with $C$ (where $C$ is the clause)
	- If $Q$ contains $\forall p$, then replace $S$ with the set containing the empty clause $\{\square\}$  

- intuitively this seems to make sense, since if you have a variable occuring on its own as a clause, and you're using a for all quantifier, there is no situation under that quantification where you satisfy all clauses for both values. Therefore the formula is false 