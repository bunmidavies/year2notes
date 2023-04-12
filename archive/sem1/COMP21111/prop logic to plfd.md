[[COMP21111]]

- propositional logic to plfd is kind of straightforward
- the domain for any variable in prop logic is $\{0,1\}$
- therefore, each atom $p$ can just be replaced with $p = 1$

- example:
  propositional formula: $\neg p \rightarrow q$
  plfd formula: $\neg p = 1 \rightarrow q = 1$

- in reality though, for plfd when $p$ is a boolean variable (i.e. $dom(p) = \{0,1\}$), we just write $p$ rather than $p = 1$


- plfd seems to be more expressive than propositional logic, but can actually be converted to prop logic. [[plfd to prop logic]]