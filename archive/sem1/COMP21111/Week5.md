[[COMP21111]]
## video 1 - Randomized Satisfiability Algorithms

***
*video 1 summary - randomized algorithms*
- random search for satisfying assignments
- one sided - these algorithms cant show unsatisfiability
- GSAT local search
- GSAT with walks
- WSAT (walk SAT)
***

- **Decision Problem**: any collections of problems that have a **yes/no** answer. Each element of this collection is called an *instance* of the problem
- E.g. : Whether a set of linear equations are solvable:
	- The **instance** is the system of linear equations
	- The answer is **yes** if there exists a solution
- Another E.g. : SAT
	- The **instance** is a finite set of clauses
	- The answer is **yes** if satisfiable, and **no** if unsatisfiable

- **Witness for an instance** : some data $D$, with which one can check in **polynomial** time if $I$ has a yes-answer given $D$ ($D$ doesn't **have** to give a yes-answer)
- Thus for satisfiability problems, witnesses = models
- However unsatisfiability has **no polynomial-size witnesses**

### CHAOS
- CHAOS is an algorithm that can establish satisfiability, but **cannot establish unsatisfiability**
- CHAOS just takes a set of clauses, a positive integer *MAX-TRIES*, and repeatedly tries random interpretations for the clauses and checks if they're satisfiable
- If CHAOS finds a model of the provided set of clauses, it will return that interpretation, otherwise it returns *don't know* after trying *MAX-TRIES* times
- **All randomized satisfiability algorithms in general cannot establish unsatisfiability**
  ![](https://i.imgur.com/bGWJRPd.png)


- To define more sophisticated random algorithms for determining satisfiability, a certain notion of how the interpretations are generated needs to be established:
	- Choose a random interpretation
	- If this interpretation isn't a model, repeatedly choose a variable and change its value (i.e. **flip** the variable from $1\rightarrow 0$ / $0\rightarrow 1$)
![](https://i.imgur.com/9IQMmmi.png)


### GSAT
- GSAT is another randomised satisfiability algorithm, taking the same inputs as CHAOS and having the same outputs
- However GSAT has additional parameters MAX-FLIPS and MAX-TRIES parameters
- Then, for MAX-TRIES number of times, pick a random interpretation and return it if it satisfies the set of clauses
- If this condition wasn't met, repeat for MAX-FLIPS: find the variable which when flipped satisfies the max no. of clauses in $S$, then modify the current interpretation and check if that interpretation is a model
- GSAT is known as a **local search algorithm**, and tries to maximise the number of satisfied clauses by local changes
![](https://i.imgur.com/N7FEAzh.png)


### GSAT example

| 0 | 0 | 1 |
| --- | --- | --- |
|$p_1$ | $\neg p_2$ | $p_3$ |
| | $\neg p_2$ | $\neg p_3$ |
| | | $\neg p_3$ |
| $\neg p_1$ | | $\neg p_3$ |
| $\neg p_1$ | $p_2$ | |
| $p_1$ | $p_2$ | |

the top row shows the random interpretation we have chosen to start with
not all clauses are satisfied, so we must begin to flip
![](https://i.imgur.com/bkm23d7.png)

at the end you see that 5/5 clauses are satisfied, so we have found a model with the algorithm this time around

- Advantages: Can quickly find satisfying assignments in large problems
- Disadvantages: Inner loops in GSAT can get stuck at points where further flips do not affect the no. of satisfied clauses

### GSAT Optimised - GSATwithWalks
- GSATwithWalks aims to optimise GSAT by preventing the local maximums where you continue to flip variables when there is no chance you will find a model
- Inputs: Set of clauses $S$ (like CHAOS and GSAT)
- Output: Model $I$ or *don't know*
- Parameters: MAX-TRIES, MAX-FLIPS, $\pi$ (a real number between 0 and 1)

- The actual algorithm is near the same as GSAT, but with an added condition:
	- When in the MAX-FLIPS loop: With probability $\pi$ pick a variable that satisfies the max no. of clauses in $S$. Then with probability $1-\pi$ randomly pick a variable that occurs in a false clause in $I$
	- Now $I = flip(I,p)$
![](https://i.imgur.com/lPLvKhk.png)


- If $\pi$ itself is 0, then there is no chance that the first condition is taken. Thus the algorithm reduces to only walks (Walk SAT)
![](https://i.imgur.com/KFHEi0v.png)


- Why does this work? Because given a false clause, you know that flipping any single variable **must make the clause true**, so you may end up with a model
- But obviously some clauses which were true previously can become false now, so you may not always progress towards a model
- All random picks are done in **uniformly random fashion**
![](https://i.imgur.com/oKi5L6b.png)


***

# video 2 - semantic tableaux

- semantic tableaux is popular across different types of logic (i.e. not just propositional logic), and is not **just** used for sets of clauses but can be applied to all kinds of formulas

- **Signed formula** - an expression $A = b$, where $A$ is a formula and $b$ is a boolean value ($0$ or $1$)
- A signed formula (A = b) is true iff given an interpretation, $I(A) = b$. So not necessarily true, just that the interpretation of A results in the same value of b

- A signed formula is satisfiable if it has a model - so for every formula $A$ and interpretation $I$, exactly one of the signed formulas $A = 1$ or $A = 0$ is true in $I$
- A formula $A$ is satisfiable if and only if the signed formula $A = 1$ is satisfiable

### semantic tableaux example

- The idea behind tableaux is to create a signed formula and break it down based off connectives
- Example: Showing satisfiability of $A\rightarrow B$ can be shown as proving satisfiability of $(A \rightarrow B) = 1$
- $(A\rightarrow B) = 1$ if and only if $A = 0$ OR $B = 1$
| $\rightarrow$ | B = 1 | B = 0 |
| --- | --- | --- |
| A = 1 | 1 | 0 |
| A = 0 | 1 | 1 |

- $(A \rightarrow B) = 0$ if and only if $A = 1$ AND $B = 0$
| $\rightarrow$ | B = 1 | B = 0 |
| --- | --- | --- |
| A = 1 | 1 | 0 |
| A = 0 | 1 | 1 |

- We can use AND-OR trees to carry out case analysis
- Tableau = a tree having signed formulas at nodes

Branch Expansion Rules
![](https://i.imgur.com/tdjooNZ.png)


When is a branch unsatisfiable/closed?
- it contains $p = 0$ and $p = 1$ for some atom $p$
- it contains $\top = 0$
- it contains $\bot = 1$
So essentially, for **any logical contradictions**

### semantic tableaux example

- $(\neg(p\lor p \rightarrow p \lor q))$
- To construct the tableau from here, your tree starts with:
	  $(\neg(p\lor p \rightarrow p \lor q)) = 1$
- Top connective is negation first, so now:
	  $(p\lor p \rightarrow p \lor q) = 0$
	*by using the branch expansion rules*
- Next top connective is implication, so:
	  $(q\lor p) = 1$
	  $(p\lor q) = 0$
- Two branches can be built off this
![](https://i.imgur.com/CkyOwIz.png)


### semantic tableaux example 2
![](https://i.imgur.com/Cmbh5yg.png)


once we have found a model, we follow the path and give all assigned variables their corresponding values, as well as any unassgined variables an arbitrary value
**note that you can choose which order to go for when applying the method, but in these examples the formulas are picked in alphabetical order**

### other properties with tableaux
- A formula $A$ is satisfiable iff a tableau for $A = 1$ contains a complete open branch (/ iff every tableau for $A = 1$ contains a complete open branch)
- A formula $A$ is valid iff there is a closed tableau for $A = 0$ (iff every tableau for $A = 0$ is closed)
- Formulas $A$ and $B$ are equivalent iff there is a closed tableau for $(A\leftrightarrow B) = 0$
- A fully expanded tableau for $A = 1$ gives all models for $A$

### flat view of tableaux