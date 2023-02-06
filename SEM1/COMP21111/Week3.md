[[COMP21111]]
 - CNF - Standard transformation to CNF
- Clausal Normal Form
- Definitional clausal transofmration
- Encoding problems as propositional satisfiability problems
- DPLL algorithm
***
[Video 1 - Literals, Clauses, CNF]
- **Literal**: an atom $p$ (positive literal) or its negation $\neg p$ (negative literal)
- Given a literal $L$, $\bar{L} = \neg p$ if $L$ is the form of $p$ (positive)
- Or $\bar{L} = p$ if $L$ is the form of $\neg p$ (negative)

- A **Clause** is made up of literals
- A clause is a disjunction $L_1 \lor ... \lor L_n, n\geq0$ of literals
- Therefore a clause is satisfiable if at least one literal can be satisfied

- There are different types of clauses:
	- Empty Clause (n = 0) is denoted as $\square$
	- Unit Clause (n = 1)
	- Horn Clause has at most **one positive literal**

- **Conjunctive Normal Form** - A formula $A$ is of CNF if it is:
	- $\bot$
	- $\top$
	- A **conjunction** of **disjunctions** - $A$ = $\land_i \lor_j L_{i.j}$

- Formula $B$ is called a CNF of formula $A$ if $A \equiv B$ and $B$ is in CNF
- Interpretation $I$ satisfies a formula in CNF *iff* it satisfies **every clause**
- Interpretation $I$ satisfies a clause *iff* it satisfies **at least one literal** $L$
- *Makes sense since CNF formula = one big conjunction, and each clause = disjunction*

- **Standard CNF Transformation** - A number of equivalences similar to what has already been seen is applied. But these are only ever applied in one direction
	- $A \leftrightarrow B \implies (\neg A \lor B) \land (\neg B \lor A)$
	- $A \rightarrow B \implies \neg A \lor B$
	- $\neg (A \land B) \implies \neg A \lor \neg B$
	- $\neg (A \lor B) \implies \neg A \land \neg B$
	- $\neg\neg A = A$
	- $(A_1 \land ... \land A_m) \lor B_1 \lor ... \lor B_n \implies (A_1 \lor B_1 \lor ... \lor B_n) \land ... (A_m \lor B_1 \lor ... \lor B_n)$

- Note for the equivalence rule, its basically just ($A \rightarrow B) \land (B \rightarrow A)$
- None of these rules are applicable once the formula:
	- Has no $\leftrightarrow$
	- Has no $\rightarrow$
	- Only has $\neg$ applied to atoms
	- Doesn't contain $\land$ within the scope of $\lor$
- **If all of these rules are met, the formula is in CNF**

- Due to the equivalence between the CNF of a formula and the original formula, it is sufficient to show the satisfiability of the CNF of a formula
- A formula in CNF will have the same models as the set containing its clauses
- **Therefore**, CNF transformation can reduce the satisfiability problem from a formula to a set of clauses

- Note that **an empty clause is unsatisfiable, but an empty set of clauses is satisfiable**

***
[Video 2 - Definitional Clausal Form transformation]

- The first part of the video demonstrates an example formula with a lot of equivalences e.g. $p_1 \leftrightarrow (p_2 \leftrightarrow (p_3 \leftrightarrow p_4))$
- What is shown is that with each equivalence, the size of the formula doubles
- Therefore the formula grows exponentially, which is a problem
- **There is no way to avoid exponential blowup with any algorithm which is finding an exact equivalent to the original**

- While focusing on satisfiability, preserving equivalence isn't actually vital
- Instead, equisatisfiability can be preserved

- **Preserving equisatisfiability**
- The main idea is **naming / definition introduction**
- A (non-literal) subformula $A$ is given a name (which doesn't appear in the original formula)
- A formula stating $A$ is equivalent to the new name is made e.g.
  $p_1 \leftrightarrow (p_2 \leftrightarrow (p_3 \leftrightarrow (p_4 \leftrightarrow (p_5 \leftrightarrow p_6))))$
  $(p_5 \leftrightarrow p_6) \leftrightarrow n$
  $p_1 \leftrightarrow (p_2 \leftrightarrow (p_3 \leftrightarrow (p_4 \leftrightarrow n)))$
- **This isn't equivalent to the original, but equisatisfiable, meaning it's satisfiable if and only if the original formula is**

- **Clausal Form** - Clausal Form of a formula $A$ is a set of clauses which is satisfiable *iff* $A$ is satisfiable
- Clausal form differs to CNF in which CNF requires the formula to be equivalent to it's original, but clausal only requires equisatisfiable
- Using clausal form algorithms will at most cause a set of clauses to grown linearly with respect to the size of the original formula

- **Definitional clausal form transformation relies on this theorem**
- $F[G]$ is satisfiable *iff* $F[n] \land (n \leftrightarrow G)$ is satisfiable, provided $n$ is a unique propositional variable not occuring in $F[G]$
- $n$ is the name / definition for $G$

[Video 3 - Proof of clausal form transformation theorem]
- In order to prove bi-implication we basically need to show that the bi implication (i.e. the *iff* in the theorem above) can go both ways
- **Proving $F[n] \land (n\leftrightarrow G)$ is satisfiable $\implies F[G]$ is satisfiable**
  Assume $F[n] \land (n\leftrightarrow G)$ is satisfiable
  So there must exist an interpretation $I$ such that $I$ is a model of $F[n] \land (n\leftrightarrow G)$
  We need to show that $F[G]$ is satisfiable
  Take $I$ then by equivalent replacement lemma we have $I$ being a model of $F[G]$

- **Proving  $F[G]$ is satisfiable $\implies$ $F[n] \land (n\leftrightarrow G)$ is satisfiable**
  Assume $F[G]$ is satisfiable
  So there must exist an interpretation $I$ such that $I$ is a model of $F[G]$
  We need to show that $F[n]\land(n\leftrightarrow G)$ is satisfiable
  Consider another interpretation
	  $I'(p) = I(p)$ if $p\neq n$ : $I(G)$ if $p = n$
  Then $I'$ is a model of $F[G]$ and $I'$ is a model of $n\leftrightarrow G$
  So then by equivalence replacement lemma, we can say $I'$ is a model of $F[n]$ (Replacing $G$ with $n$)
  And therefore $I'$ is a model of $F[n] \land (n\leftrightarrow G)$, so it must be satisfiable
  
- **Definitional clausal form transformation steps**
	- Give names for every non-literal subformula (this creates a linear number of new names)
	- Replace subformulas in o.g. formula with their name (and state which is which)
	- Use the standard CNF transformation to transform the symbols/resulting definitions into clauses

- **Definitional clausal form transformation theorem** - Any propositional formula can be transformed into an equisatisfiable clausal normal form, by applying the definitional clausal form transformation
- The size of the resulting clause set is linear in size of the original formula, and each clause has at most 3 literals

- **Optimising definitional clausal transformation**
- Using the polarity learned from Week2, we find that if a subformula has positive or negative polarity, implication can be used instead of equivalence for the definition: $F[G]$ is satisfiable *iff* $F[n] \land (n\leftrightarrow G)$
- This can simplify a number of definitions while performing the definitional clausal form transformation

***
[Video 4 - formalising problems using propositional logic]

- If we have variables $v_1,...,v_n$, and we want to express exactly $k$ are true, then we can encode this:
- $T_{=k}(v_1,...,v_n)$ to express $k$ of $n$ variables are true
- $T_{\leq k}(v_1,...,v_n)$ to express **at most** $k$ of $n$ variables are true
- $T_{\geq k}(v_1,...,v_n)$ to express **at least** $k$ of $n$ variables are true