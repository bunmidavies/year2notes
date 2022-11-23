[[COMP21111]]

# equivalence replacement

**Equivalent Replacement Lemma:**
	*Let $I$ be an interpretation and $I \vDash A_1 \leftrightarrow A_2$. Then $I\vDash B[A_1] \leftrightarrow B[A_2]$* 
- **Notation**: $A[B]$ = formula $A$ with fixed occurence of formula $B$. Therefore $A[B']$ is the formula obtained from $A$ by replacing the occurence of $B$ with $B'$
- The lemma means by replacing $A_1$ with $A_2$ given they're equivalent, the syntactic structure is irrelevant thus the value of the resulting formula stays the same
- This becomes the **Equivalent Replacement Theorem**:
	  *Let $A_1 \equiv A_2$. Then $B[A_1] \equiv B[A_2]$.

- There are several connections that can be made based off the notions of equivalence, satisfiability and validity. For instance:
	1. $A$ is valid if and only if $\lnot A$ is unsatisfiable
	2. $A$ is valid if and only if $A$ is equivalent to $\top$

	3. $A$ is satisfiable if and only if $\lnot A$ is not valid
	4. $A$ is satisfiable if and only if $A$ is not equivalent to $\bot$

	5. $A$ and $B$ are equivalent if and only if $A\leftrightarrow B$ is valid
	
	6. $A$ and $B$ are equivalent if and only if $\lnot (A\leftrightarrow B)$ is unsatisfiable

- Note that **validity = tautology**
- These properties allow us to decompose formulas in ways that allow us to determine satisfiability / validity / equivalence using one or the other
- Propositional satisfiability is NP-complete, and propositional validity is coNP-complete

- If given a formula consisting of only $\top$ and $\bot$, by using equivalences the formula can be simplified. This is known as the **rewrite rule system**, e.g.:
	- $\top \land ... \land \top$ = $\top$
	- $\bot \land A_1 \land ... \land A_n = \bot$
	- $\top \lor A_1 \lor ... \lor A_n$ = $\top$
	- $\bot \lor ... \lor \bot$ = $\bot$
	- $\lnot \top = \bot$ and $\lnot \bot = \top$
	- $A \rightarrow \top = \top$
	- $\bot \rightarrow A = \top$
	- $\top \rightarrow \bot = \bot$
	- Basic equivalences (e.g. $\top \leftrightarrow \top$ etc)

- Therefore, using the rewrite rules, a purely syntactic algorithm can be used in order to evaluate a formula, given formula $A$ and interpretation $I$
  
```
for all atomic formulas p in A:
	if I satisfies p
		replace all occurences of p in A with TRUE
	else
		replace all occurences of p in A with FALSE

rewrite A into normal form using system rules

if A = TRUE return 1
else return 0
```

- Using this formula and rules either **inside-out**/**outside-in** from left to right or vice versa, you'll always end up with either true or false. The result will always be the same regardless of the rewrite order, but sometimes different orders can take longer than others

## QBF equivalent replacement
- let $I$ be an interpretation and $I \models F_1 \leftrightarrow F_2$. Then $I \models G[F_1] \leftrightarrow G[F_2]$
- Let $F_1 = F_2$. Then $G[F_1] = G[F_2]$
- *given two equivalent formulas, they can be replaced in a bigger formula, obtaining equivalent formulas for both*