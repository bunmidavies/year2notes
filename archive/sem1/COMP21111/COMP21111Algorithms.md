[[COMP21111]]

exhaustive list of all COMP21111 algorithms + other vaguely related properties / rules, attempted to be kept in chronological order in terms of course weeks

***

### definitional clausal form transformation

![](https://i.imgur.com/DMDtmrx.png)


### clausal normal form optimisation

![](https://i.imgur.com/2Fb569D.png)


***

### DPLL for propositional formulas

![](https://i.imgur.com/wnGXjm1.png)


***

## random satisfiability algos
- **none of these can establish unsatisfiability**

- To define more sophisticated random algorithms for determining satisfiability, a certain notion of how the interpretations are generated needs to be established:
	- Choose a random interpretation
	- If this interpretation isn't a model, repeatedly choose a variable and change its value (i.e. **flip** the variable from $1\rightarrow 0$ / $0\rightarrow 1$)
![](https://i.imgur.com/pMkIjDw.png)


### CHAOS

![](https://i.imgur.com/bL2Ra94.png)



### GSAT
![](https://i.imgur.com/1YmDh1v.png)

![](https://i.imgur.com/Yhzamdn.png)


### GSATwithWalks

![](https://i.imgur.com/e8gphZk.png)

- with probability $1 - \pi$, you are selecting a random variable which appears in a clause which evaluates to false in the set of clauses (its kind of worded weirdly in the screenshot) - when you flip this, then youre obviously going to change the outcome of that clause from false to true

### WalkSAT

- when $\pi = 0$ for GSATwithWalks, GSATwithWalks technically reduces to WSAT (only walks)
![](https://i.imgur.com/533qQf6.png)


***

### semantic tableaux rules for propositional formulas

![](https://i.imgur.com/swkgH8M.png)


***
# BDTs / BDDs / OBDDs

properties of binary decision trees:
![](https://i.imgur.com/47RZpjJ.png)


### build BDT
![](https://i.imgur.com/Wz83MJ1.png)


properties of BDDs
![](https://i.imgur.com/tkbix48.png)


properties of OBDDs
![](https://i.imgur.com/PwD6gUu.png)


### integrate
![](https://i.imgur.com/dFr6wQ8.png)


### build OBDD
![](https://i.imgur.com/IzERdGg.png)



### OBDD disjunction
![](https://i.imgur.com/UOEFt1f.png)


### OBDD conjunction
![](https://i.imgur.com/CmJYoIr.png)


***
### Rectification / Renaming
![](https://i.imgur.com/weIhe0a.png)



### Prenexing rules
![](https://i.imgur.com/M0WqfvD.png)



### DPLL for QBFs

![](https://i.imgur.com/HiWQOYf.png)


- basic steps: Apply unit propagation, evaluate the current set of clauses, select the outermost quantified variable and delete the quantifier, then call the algorithm recursively with this new unit clause (which we either make true or false)
- think of disjunction and conjunction to understand why we can determine that the formula is true after obtaining $(1,\exists)$ or false after obtaining $(0,\forall)$
- remember for unit propagation, if the quantifier contains $\forall p$ and the set of clauses contains the unit clause $p$, we can immediately determine this set of clauses is unsatisfiable

example:
![](https://i.imgur.com/RIalRw0.png)


### Optimisations for DPLL for QBFs

#### pure literal rule
![](https://i.imgur.com/0eJpUML.png)


#### universal literal deletion
![](https://i.imgur.com/73qWscC.png)


***

### converting QBFs to OBDDs

![](https://i.imgur.com/RV89MWh.png)


![](https://i.imgur.com/sC9Qcr3.png)


### converting PLFD to prop. logic

![](https://i.imgur.com/ef4D8YQ.png)


### PLFD tableau rules

![](https://i.imgur.com/hZved0a.png)



***
`week 11`

![](https://i.imgur.com/k4PVu48.png)

- F returns whether the given state is a final state or not
- I denotes the initial states 
- R is the reachability condition
![](https://i.imgur.com/1wPIDCv.png)


![](https://i.imgur.com/sa9Yd8h.png)

![](https://i.imgur.com/kDD7kuX.png)


![](https://i.imgur.com/kqpB0By.png)
