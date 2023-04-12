# semantics

- Semantics are defined using interpretations (truth assignments) - a mapping that assigns values to variables
- Therefore an interpretation itself is a function
  $I : P \rightarrow \{1,0\}$
- All formulas can essentially be mapped into a truth value recursively
	  - $I(\top) = 1$  & $I(\bot) = 0$ 
	  - $I(A_1 \land ... \land A_n) = 1$ if and only if $I(A_i) = 1$ for all $i$ (conjunction)
	  - $I(A_1 \lor ... \lor A_n) = 1$ if and only if $I(A_i) = 1$ for at least one $i$ (disjunction)
	  - $I(\lnot A) = 1$ if and only if $I(A) = 0$
	  - $I(A_1 \rightarrow A_2) = 1$ if and only if $I(A_1) = 0$ or $I(A_2) = 1$
	  - $I(A_1\leftrightarrow A_2) = 1$ if and only if $I(A_1) = I(A_2)$

- *Implication works in the sense that an implication is only false when you have a true statement that implies a false statement. The implication doesn't work here because then you haven't implied anything - you've just stated a true statement and then stated something which isn't true, which a true statement couldn't have implied*
- Models: $I \vDash A$ if $I(A) = 1$ 
- $I \nvDash A$ if $I(A) = 0$
- Truth tables and operation tables are both used for defining semantics of propositional logic - operational tables look at the actual truth values and their connectives, while truth tables consider all propositional variables within a formula

- Because every formula is essentially a function over truth values, you can basically infer that **any function over truth values can be represented using a propositional formula**

- Formulas can be evaluated over interpretations (basically just like providing parameters to a function). **The algorithm required to do this can run in linear time O(N)**, however algorithms required to determine satisfiability will not be linear

***

# satisfiability / validity / equivalence

- As mentioned within the semantics section, if formula $A$ is true in interpretation $I$ we can say that:
	- $I$ satisfies $A$
	- $I$ is a model of $A$. $I \vDash A$
- If a formula $A$ is false in interpretation $I$ then $I$ does not satisfy $A$. $I \nvDash A$
- **Satisfiable** - $A$ is **satisfiable** if it is true in at least one interpretation
- **Unsatisfiable** - $A$ is **unsatisfiable** if there is no interpretation in which $A$ is true
- By being unsatisfiable, this technically means $\bot$ is a model of A, since $A$ is false in all interpretations

- If a formula $A$ is true in all interpretations, then it is a tautology ($\vDash A$)
- $A$ *entails* $B$ if all models of $A$ are models of $B$ (therefore a subset, this is not the same as equivalence)
- $A$ *is equivalent* to $B$ if $A$ and $B$ have the same models. $A \equiv B$.

- Truth tabling is the most common way to determine satisfiability / validity / equivalence 
- The main problem with truth tables is that they don't scale well - truth tables need $2^n$ rows, where $n$ is the number of propositional variables in the formula

- Equivalences hold if we substitute any formulas

***

