[[COMP21111]]

Quantification: given an [[OBDD]] representing a formula $F$, generate an OBDD representing $\forall / \exists p_1 ... \forall / \exists p_n F$ 

the following properties of QBFs are used:
	- $\exists p$ (if $p$ then $F$ else $G$) = $F \lor G$
	- $\forall p$ (if $p$ then $F$ else $G$) = $F \land G$
and if $p \neq q$ then
	- [q]$p$ (if $q$ then $F$ else $G$) = if $q$ then [q]$pF$ else [q]$pG$
	- where [q] is any quantifier

## existential quantification

![](https://i.imgur.com/YDvLKbg.png)


- remember that `max_atom` returns the maximum variable in the ordering for the OBDD

## universal quantification
``
![](https://i.imgur.com/ByW3AMP.png)


- quantification is also known as **quantifier elimination**, as we have the ability to remove quantifiers from a boolean formula and produce an equivalent, quantifier-free formula
- by using these algorithms on OBDDs we can check the satisfiability/validity of QBFs
- evaluation/satisfiability/validity of QBFs is pspace-complete
- **we eliminate quantifiers from innermost to outermost using OBDDs, this differs to DPLL/splitting**