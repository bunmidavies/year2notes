[[COMP21111]]

![](https://i.imgur.com/aDF4AaF.png)


## splitting example: $\forall p \exists q(p\leftrightarrow q)$

*this formula is in prenex normal form, and is rectified, so we can use the splitting algorithm*

![](https://i.imgur.com/nr49fis.png)


- note that in **conjunction** branches, we have to find $1$ for both branches
- in **disjunction** branches, we only have to find $1$ in a branch, then we can stop and evaluate the parent node as $1$
- for this reason, the order of variables is important!