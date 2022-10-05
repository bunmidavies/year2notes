# Propositional Satisfiability Problem
- Given a propositional formula $A$, we want to check whether it is satisfiable or unsatisfiable
- If $A$ is satisfiable, we want to find a satisfying assignment for $A$ (A model of $A$)
- It's the first ever problem to be proved **NP-Complete**
- Propositional logic can be applied to many problems, one including the russian spy problem shown in the first video, or circuit equivalence (also shown in the first video)

# Satisfiability algorithms
- The main difference between evaluation algorithms and satisfiability algorithms using a truth table is that with evaluation algorithms we are just trying to find the result of a certain interpretation, meanwhile for satisfiability we are trying to find an interpretation which is a model of the propositional formula
- The major drawback once again of all truth tables is scaling - we can try and solve this formula by using a compact truth table, which allows you to explore all possible values of the formula, without exploring all possible values of the propositional variables
- The key to satisfiability algorithms is guessing variable values and propagation


# Splitting Algorithm (satisfiability algorithm)
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

# Monotonicity, position, polarity


# Monotonic replacement / pure atom rule
