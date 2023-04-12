[[COMP21111]]

- LTL is a type of logic to express properties of paths in a [[computation tree]]
- specifically - for some state on the path, for every two consecutive states

## LTL definition
- $\top$ and $\bot$ are formulas
- every atom $x = v$ of [[plfd]] is an atom in LTL
- if $A_1,...,A_n$ are formulas, where $n \geq 2$, then $(A_1\land ... \land A_n)$ and $(A_1\lor ... \lor A_n)$ are too
- if $A$ is a formula then $\neg A$ is a formula
- if $A$ and $B$ are formulas, $(A\rightarrow B)$ and $(A\leftrightarrow B)$ are too

- if $F$ is a formula, then $\bigcirc F$, $\square F$ and $\Diamond F$  are formulas
- if $F$ and $G$ are formulas, then $F  \mathcal{U}  G$  is a formula and $F\mathcal R G$ are formulas

## LTL connectives
![](https://i.imgur.com/mxE4sXk.png)


# [[LTL semantics]]