[[COMP21111]]

- Let $p$ be a boolean variable and $F_\pi = p$
	- The occurence of $p$ at the position $\pi$ in $F$ is **bound** if $\pi$ can be represented as the concatenation of two strings $\pi_1 \pi_2$ (2 positions?) such that $F_{\pi_1}$ has the form $\forall pG$ or $\exists pG$ for some $G$
	- **in simpler terms** - an occurence of $p$ is called **bound** if a quantifier appeared earlier

- Free = not bound
- A variable can be both *free* and *bound* in a given formula, since to be free there must be one free occurence, but also to be bound there must be one bound occurence
- A formula is called *closed* if it has no free variables at all - [[QBF - closed formulas]]
