## video 1 - Randomized Satisfiability Algorithms

- Decision Problem: any collections of problems that have a **yes/no** answer. Each element of this collection is called an *instance* of the problem
- E.g. : Whether a set of linear equations are solvable:
	- The **instance** is the system of linear equations
	- The answer is **yes** if there exists a solution
- Another E.g. : SAT
	- The **instance** is a finite set of clauses
	- The answer is **yes** if satisfiable, and **no** if unsatisfiable
- **Witness for an instance** : some data $D$, with which one can check in **polynomial** time if $I$ has a yes-answer given $D$ ($D$ doesn't **have** to give a yes-answer)
- So for the satisfiability problems, **witness = interepretation**
- However unsatisfiability has **no polynomial-size witnesses**

### CHAOS
- Satisfiability algorithm which can't establish unsatisfiability: $CHAOS$
- CHAOS just takes a set of clauses, a positive integer *MAX-TRIES*, and repeatedly tries random interpretations for the clauses and checks if they're satisfiable
- If CHAOS finds a model of the provided set of clauses, it will return that interpretation, otherwise it returns *don't know* after trying *MAX-TRIES* times
- **Randomized satisfiability algorithms in general cannot establish unsatisfiability**

- Switching between random interpretations:
- Choose a random interpretation, then if this interpretation is not a model, repeatedly choose a variable and *change its value in the interpretation (**flip the variable**)*

### GSAT
- GSAT is another randomised satisfiability algorithm
- It takes a set of clauses as input, as well as  MAX-FLIPS and MAX-TRIES parameter