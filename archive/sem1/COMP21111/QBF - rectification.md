- rectification is a syntactical process, and involves substitution, as mentioned in [[QBF - substitution]]

- the first aim of rectification is to have a quantified boolean formula where no variable has both **bound** and **free** occurences ([[QBF - bound and free]])
- the second aim of rectification is to make sure no variable is **quantified multiple times**

- **rectification preserves equivalence**

- a rectified formula $F$
	- has no variable which appears both free and bound in $F$
	- for every variable $p$, $F$ contains at most one occurence of a quantifier of $p$

- **jointly rectified formulas** $(F_1,...,F_n)$:
	- if $p$ occurs free in one of $F_i$ then $p$ doesnt occur bound in $F_1,...F_n$
	- theres at most one occurence of quantifiers of $p$ in $F_1,...,F_n$
- where $p$ is every variable in each formula

### Example
![](https://i.imgur.com/3DhCy2q.png)

- on the first line, you see that $p$ occurs bound and free, and has a quantification within another quantification
- $p$ in the $\forall$ part is renamed to $p_1$, so now the multiple quantification is gone, but the free and bound occurence of $p$ still remains
- $p$ in the $\exists$ part is renamed to $p_2$, so now there are no mixed bound/free occurences of a variable, and no multiple quantification