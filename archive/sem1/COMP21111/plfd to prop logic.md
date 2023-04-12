[[COMP21111]]

- basically, the opposite / slightly more difficult direction (the easier being [[prop logic to plfd]])

## plfd to prop logic

- take plfd formula $F$

- for each variable $x$, introduce a propositional variable $x_v$ **for each $v \in dom(x)$**
e.g. $dom(x) = \{a,b,c\}$
corresponding prop variables: $x_a,x_b,x_c$

- each atom $x = v$ is replaced by $x_v$. this results in a new prop formula, $F_{prop}$

- in order to solidify the fact that each variable **must** take exactly one value, a **domain axiom** can be used:

$$(x_{v_1} \lor ... x_{v_n}) \land \land_{i<j} (\neg x_{v_i} \lor \neg x_{v_j})$$
<span id="important"> the first part assures that the variable has a value, and the second part assures that no two distinct prop variables are 1 at the same time (i.e. no plfd variable has two different values at once)</span>

- $D_{all}$ is used to denote the conjunction of all domain axioms (i.e. for all variables in $F$)

- using this, the plfd formula $F$ is satisfiable if and only if propositional formula $F_{prop} \land D_{all}$ 

## example

$dom(x) = \{a,b,c\}$. if we want to check the satisfiability of the following:
$$\neg(x = b \lor x = c)$$
, we have to check the satisfiability of the following:
$$(x_a \lor x_b \lor x_c) \land (\neg x_a \lor \neg x_b) \land (\neg x_a \lor \neg x_b) \land (\neg x_a \lor \neg x_c) \land (\neg x_b \lor \neg x_c) \land \neg(x_b \lor x_c)$$
and so this can be done with the regular methods (e.g. [[DPLL - QBFs and Propositional]])