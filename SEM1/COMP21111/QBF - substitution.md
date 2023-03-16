[[COMP21111]]

- there are a number of problems that can occur when trying to use normal substitution methods for variables in a QBF, like you would with a propositional formula
- you can't just substitute variables as you do for propositional formulas, as you end up with nonsense

- the next solution is to only replace free variables in a formula, without worrying about the bound variables, but we want variables that aren't both free and bound for rectification [[QBF - rectification]]

- the solution to above is to **rename bound variables**
  ![](https://i.imgur.com/GpQYkIj.png)
  
- symbol 1 means **any quantifier**, and symbol 2 means **and / or**

- this is the process for renaming bound variables (note that $F[EApG]$ is just formula $F$ which contains some quantified subformula $G$)
	1. Replace all free occurences of $p$ in $G$ with a fresh variable $q$ ($G$ itself doesn't involve the quantifier, which is why its *free* occurences)
- This gives $F[EAqG']$ as the result
*$EA$ is just how im describing the ~any quantifier~ symbol above*

  
