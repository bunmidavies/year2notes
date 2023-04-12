[[COMP21111]]

- Propositional logic is the foundation for most of the more expressive logics, it is a simpler version of expressing logic but has many computational challenges
- Propositional logic can be directly applied to things like maths and circuit design

- **Syntax** = the formality and rules to the language
- **Semantics** = the meaning of the language
- **Reasoning** = proof theory and model theory

- Connectives = $\land$,$\lor$,$\lnot$,$\rightarrow$,$\leftrightarrow$
- Immediate subformulas of a formula are the formulas which are affected by the first connective
- Example: $((p\land q)\rightarrow(q\lor \lnot p \lor s))$
  The immediate subformulas here are:
  - $(p\land q)$
  - $(q\lor \lnot p \lor s)$
  The connective of these two being $\rightarrow$

- $A[B]$ means that $B$ occurs in $A$ as a subformula (immediate or non immediate)

- **precedence** and levels of precedence are introduced to remove ambiguity and occassionally be able to drop brackets when they aren't needed
- [[connective precedence]]

- This **isn't part of the logic itself**, we use this for convenience (as said in Week1Video2)
- By using precedence we can *parse formulas*:
	- Inside-out = highest precedence connectives first (i.e. **Negation first**)
	- Outside-in = lowest precedence connectives first (i.e. **Equivalence first**)
- You take the **largest subformula** on each side of the connective in order to parse outside-in, and you take the **smallest subformula** on each side of the connective in order to parse inside-out

- More in [[propositional logic semantics]]