[[COMP21111]]

==Pure atom== - An atom (propositional variable) is pure in a certain formula, given that all occurences of it are positive, or all are negative (in terms of polarity). You can once again determine this using colouring method within parse trees

- **Pure atom rule** - An atom *p* having only positive occurences in $A$ implies $A$ is satisfiable if and only if so is $A^\top_p$
	- When all occurences are negative = Replace with $\bot$
	- When all occurences are positive = Replace with $\top$
- This can be proved by applying the **monotonic replacement theorem**
- This theorem allows you to replace certain variables with $\top$ / $\bot$, and still satisfy interpretations as you would with the variables included