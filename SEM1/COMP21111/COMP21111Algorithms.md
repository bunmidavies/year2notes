exhaustive list of all COMP21111 algorithms + other vaguely related properties / rules, attempted to be kept in chronological order in terms of course weeks

***

### definitional clausal form transformation

![[Pasted image 20230123195537.png]]

### clausal normal form optimisation

![[Pasted image 20230123200745.png]]

***

### DPLL for propositional formulas

![[Pasted image 20230123203530.png]]

***

## random satisfiability algos
- **none of these can establish unsatisfiability**

- To define more sophisticated random algorithms for determining satisfiability, a certain notion of how the interpretations are generated needs to be established:
	- Choose a random interpretation
	- If this interpretation isn't a model, repeatedly choose a variable and change its value (i.e. **flip** the variable from $1\rightarrow 0$ / $0\rightarrow 1$)
![[Pasted image 20221106165221.png]]

### CHAOS

![[Pasted image 20230123213759.png]]


### GSAT
![[Pasted image 20230123214302.png]]
![[Pasted image 20230123215828.png]]

### GSATwithWalks

![[Pasted image 20230123220045.png]]
- with probability $1 - \pi$, you are selecting a random variable which appears in a clause which evaluates to false in the set of clauses (its kind of worded weirdly in the screenshot) - when you flip this, then youre obviously going to change the outcome of that clause from false to true

### WalkSAT

- when $\pi = 0$ for GSATwithWalks, GSATwithWalks technically reduces to WSAT (only walks)
![[Pasted image 20230123220418.png]]

***

### semantic tableaux rules for propositional formulas

![[Pasted image 20230122063332.png]]

***
# BDTs / BDDs / OBDDs

properties of binary decision trees:
![[Pasted image 20230123225209.png]]

### build BDT
![[Pasted image 20230123225249.png]]

### BDT to BDD
![[BDTtoBDD.gif]]

properties of BDDs
![[Pasted image 20230123225941.png]]

properties of OBDDs
![[Pasted image 20230123230410.png]]

### integrate
![[Pasted image 20230123230606.png]]

### build OBDD
![[Pasted image 20230123230721.png]]


### OBDD disjunction
![[Pasted image 20230123232406.png]]

### OBDD conjunction
![[Pasted image 20230123233322.png]]

***
### Rectification / Renaming
![[Pasted image 20230124102846.png]]


### Prenexing rules
![[Pasted image 20230124102709.png]]


### DPLL for QBFs

![[Pasted image 20230122190317.png]]

- basic steps: Apply unit propagation, evaluate the current set of clauses, select the outermost quantified variable and delete the quantifier, then call the algorithm recursively with this new unit clause (which we either make true or false)
- think of disjunction and conjunction to understand why we can determine that the formula is true after obtaining $(1,\exists)$ or false after obtaining $(0,\forall)$
- remember for unit propagation, if the quantifier contains $\forall p$ and the set of clauses contains the unit clause $p$, we can immediately determine this set of clauses is unsatisfiable

example:
![[Pasted image 20230122191936.png]]

### Optimisations for DPLL for QBFs

#### pure literal rule
![[Pasted image 20230122192216.png]]

#### universal literal deletion
![[Pasted image 20230122193835.png]]

***

### converting QBFs to OBDDs

![[Pasted image 20230122202230.png]]

![[Pasted image 20230122202304.png]]

### converting PLFD to prop. logic

![[Pasted image 20230122203825.png]]

### PLFD tableau rules

![[Pasted image 20230122204243.png]]


***
`week 11`

![[Pasted image 20230123160303.png]]
- F returns whether the given state is a final state or not
- I denotes the initial states 
- R is the reachability condition
![[Pasted image 20230123160715.png]]

![[Pasted image 20230123170744.png]]
![[Pasted image 20230123170800.png]]

![[Pasted image 20230123194145.png]]