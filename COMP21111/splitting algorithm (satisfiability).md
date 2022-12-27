[[COMP21111]]

Splitting Algorithm (satisfiability algorithm)
- $A^{\bot}_{p}$ means the formula $A$, where all occurences of the propositional variable $p$ are replaced with $\bot$
- Essentially $A^{Replacement}_{ToReplace}$ 
- Lemma
  $p$ is a propositional variable, $A$ is a formula, and $I$ is an interpretation
  1. If $I \vDash p$, then $I \vDash p \leftrightarrow \top$ ($p$ is equivalent to $\top$)
  Equivalent replacement lemma means $A$ is equivalent to $A^{\top}_{p}$ in $I$
  2. If $I \nvDash p$, then $I \vDash p \leftrightarrow \bot$ ($p$ is equivalent to $\bot$)
  Equivalent replacement lemma means $A$ is equivalent to $A^{\bot}_{p}$ in $I$

- Splitting step: pick a variable $p$ and perform case analysis:
	- Replace p with $\top$ or $\bot$, and then simplify the formula (using simplification rules)
	- Repeat this step while the formula doesn't evaluate to true (basically recursing until a satisfiable interpretation is found, or all paths have been exhausted, thus returning false)
	- If a true value is found, the model (interpretation which evaluates to true) is just found by copying the path/choices made on the branch which terminates at $\top$