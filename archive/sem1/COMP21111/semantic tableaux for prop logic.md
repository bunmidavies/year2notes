[[COMP21111]]

Signed formula: $A = b$  where $A$ is a formula and $b$ is a boolean value
A signed formula is true in an interpretation $I$ if $I(A) = b$
So for every formula and interpretation, exactly one of the signed formulas $A = 1$ or $A = 0$ is true in this interpretation

AND-OR trees can be used to carry out case analysis on any prop. formula

![](https://i.imgur.com/ctOWVd8.png)


Branches are denoted with the bar | (signifying OR)

a branch is closed in the tree to indicate the set of signed formulas are unsatisfiable
This happens when:
- the branch contains both $p = 0$ and $p = 1$ for some atom $p$
- it contains $\top = 0$
- it contains $\bot = 1$


remember, you should aim to branch ==as late as possible== when drawing the tree

a branch is ==open== when you have applied all rules and dont reach a contradiction - this means that the signed formula is satisfiable, and any variables you didnt assign along this path can have any value (the rest need to be as assigned on the path)

a formula is valid iff there is a closed tableau for $A = 0$ (iff every tableau is closed)

$A$ and $B$ are equivalent if there is a closed tableau for $(A\leftrightarrow B) = 0$

the fully expanded tableau for $A = 1$ gives all models for $A$