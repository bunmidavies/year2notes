[[COMP24011]] / #comp24011

- A **probability assignment** $p$ is a function mapping any proposition in an agent's language to a number
  $$p(\phi)\in [0,1]$$
- $p$ obeys the following:
	1. If $\phi$ is a tautology ($\models \phi$) then $p(\phi) = 1$
	2. If $\neg (\phi \land \beta)$ is a tautology then $p(\phi \lor \beta)$ = $p(\phi) + p(\beta)$