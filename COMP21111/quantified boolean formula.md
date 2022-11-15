- quantified boolean formulas extend [[propositional formula]]
- **example**: in a 2 player game, with players $P$ and $Q$, where $P$ aims to make formula $G$ true, and $Q$ aims to make formula $G$ false, we say that $P$ has a winning strategy if:
	- There exists a move for $P$ such that:
	- For all moves of $Q$:
	- There exists a move $P$ such that:
	- For all moves of $Q$
	- ...
	- For all moves of $Q$, formula $G$ becomes true
- i.e. $\exists p_1 \forall q_1 \exists p_2 \forall q_2 ... \exists p_n \forall q_n G$

- Definition:
	- If $p$ is a boolean variable and $F$ is a formula, then $\forall pF$ and $\exists pF$ are formulas
	- Existentially quantified = $\exists$
	- Universally quantified = $\forall$

- refer to [[variable assignment definition]] for understanding on the $I^b_p(q)$ notation
- Extended semantics:
	- $I(\forall pF) = 1$ if and only if $I^0_p(F) = 1$ and $I^1_p(F) = 1$
	- $I(\exists pF) = 1$ if and only if $I^0_p(F) = 1$ or $I^1_p(F) = 1$

- Extended subformulas + position and polarity
	- The formula $F_1$ is the immediate subformula of the formulas $\forall pF_1$ and $\exists pF_1$
	- Quantifiers are like unary connectives. Subformulas with quantifiers have the same polarity as the parent (?) formulas
- Further info on bound / free - [[QBF - bound and free]]

- note that [[equivalent replacement]] holds for QBFs as well as propositional formulas