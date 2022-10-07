# syntax

- Propositional logic is the foundation for most of the more expressive logics, it is a simpler version of expressing logic but has many computational challenges
- Propositional logic can be directly applied to things like maths and circuit design

- Syntax = the formality and rules to the language
- Semantics = the meaning of the language
- Reasoning = proof theory and model theory

- Propositional statements can be built from atomic propositions using boolean connectives (and, or, not, ...)
- Propositions can be **true** or **false**
- Propositional variable = propositional formula = atomic formula = atom

- Connectives = $\land$,$\lor$,$\lnot$,$\rightarrow$,$\leftrightarrow$
- Immediate subformulas of a formula are the formulas which are affected by the first connective
- Example: $((p\land q)\rightarrow(q\lor \lnot p \lor s))$
  The immediate subformulas here are:
  - $(p\land q)$
  - $(q\lor \lnot p \lor s)$
  The connective of these two being $\rightarrow$

- $A[B]$ means that $B$ occurs in $A$ as a subformula (immediate or non immediate)

- **precedence** and levels of precedence are introduced to remove ambiguity and occassionally be able to drop brackets when they aren't needed
- The order of precedence goes (from first priority being 1):
	  1. Negation $\lnot$
	  2. Conjunction $\land$
	  3. Disjunction $\lor$
	  4. Implication $\rightarrow$
	  5. Equivalence $\leftrightarrow$

- This **isn't part of the logic itself**, we use this for convenience (as said in Week1Video2)
- By using precedence we can *parse formulas*:
	- Inside-out = highest precedence connectives first (i.e. **Negation first**)
	- Outside-in = lowest precedence connectives first (i.e. **Equivalence first**)
- You take the **largest subformula** on each side of the connective in order to parse outside-in, and you take the **smallest subformula** on each side of the connective in order to parse inside-out

***

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

# equivalence replacement

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

- Equivalent Replacement Lemma:
	*Let $I$ be an interpretation and $I \vDash A_1 \leftrightarrow A_2$. Then $I\vDash B[A_1] \leftrightarrow B[A_2]$* 
- **Notation**: $A[B]$ = formula $A$ with fixed occurence of formula $B$. Therefore $A[B']$ is the formula obtained from $A$ by replacing the occurence of $B$ with $B'$
- The lemma means by replacing $A_1$ with $A_2$ given they're equivalent, the syntactic structure is irrelevant thus the value of the resulting formula stays the same
- This becomes the **Equivalent Replacement Theorem**:
	  *Let $A_1 \equiv A_2$. Then $B[A_1] \equiv B[A_2]$.*

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