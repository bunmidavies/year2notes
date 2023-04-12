[[COMP21111]]

- DPLL algorithm
- DPLL optimisations - tautology elimination
***
## Video 1 - DPLL algo

- The DPLL algorithm is widely used in industry, and involves two main steps:
	1. Unit Propagation
	2. Splitting?

- **Unit Propagation**
  Let $S$ be a set of clauses
  Now, repeatedly perform the following transformation:


  *If $S$ contains a unit clause (a clause with one literal $L$), then:
	  ->Remove from S all clauses which have the form $L \lor C$
	  ->Replace in S all clauses of the form $\bar{L}\lor C$ with $C$*	  


- i.e. remove all clauses containing the exact literal, and remove the literal itself from the clause if it is the negation
- Unit Propagation preserves satisfiability while these transformations take place
- **If we end up with a unit (another clause which is just a literal) as the result of propagating one unit, we need to propagate that new unit**
- We obtain an empty clause where we end up with a clause where **all literals have been removed** - UNSATISFIABLE
- We obtain the empty set of clauses where we have removed all clauses - SATISFIABLE

- **Drawing DPLL trees**
- In the root node, we write all clauses
- If we have no unit clause, we just select one literal, and add it at the top of the list of clauses in a new node branching off to the left/right

- We extract the model for a set of clauses by collecting all selected literals and literals used in unit propagation, all while following the branch which led to an empty set (empty set is **satisfiable**, empty clause is **unsatisfiable**)
- If the literal doesnt appear along the path, you can just give it any value (but 0 probably makes more sense?)

- **Empty Clause = Unsatisfiable**
- **Empty Set of Clauses = Satisfiable**

***
## Video 2 - Optimising the DPLL algorithm

- **Tautology elimination**
- Tautologies are valid formulas, and all tautological clauses have the form 
	$p \lor \neg p \lor C$ (variable and negation of same variable exist within same clause)
- **This is the only form a tautology can take**
- Because tautological formulas are always true, we can remove them from clause sets without affecting satisfiability



- **Horn Clauses**
- A clause is called a **Horn Clause** if the clause contains at most 1 positive literal
- A positive literal is a non negated literal (positive polarity)
- example:
  $p_1$
  $\neg p_1 \lor p_2$
  $\neg p_1 \lor \neg p_2 \lor p_3$
  $\neg p_3 \lor \neg p_4$
- If we have a horn clause, deleting a literal will always result in another horn clause (we cant gain positive literals by removing literals)

***
## Video 3 - Random Satisfiability

- **SAT** is a problem of satisfiability checking for sets of clauses.
- A k-clause is a **clause** with *k* **literals**. *k-SAT* is the problem of satisfiability checking for sets of k-clauses

- SAT is **NP-complete**
- 3-SAT is **NP-complete**
- 2-SAT is decidable in **linear time**

- All SAT problems can be reduced to 3-SAT based on the naming method (the method used to actually create the clausal tables)

- **Generating random k-clauses**
- A random clause is a collection of random literals
- Firstly, a random literal is generated - create a fixed number of boolean variables, then select one of these, where each boolean variable has **an equal probability of being selected**
- Given that every literal has itself and its negation, the prob of selecting a single variable is $1/2n$, where $n$ is the number of variables
- Now, to generate the actual k-clause: generate k random literals as described above

- As you add clauses, the number of models for a set of clauses will stay the same (if tautology) or decrease. Therefore you are transitioning from **satisfiable** to **unsatisfiable**

- **Calculating probability of a 3-clause being unsatisfiable**
- We have $n$ boolean variables, $m$ clauses, and are generating $m$ clauses with equal probability
- Probability of generating unsatisfiable clause ($\pi$)=
  $$\frac{\#unsat}{\#all}$$
- Where unsat = no of unsatisfiable clauses, and all = no of all clauses
- An important parameter is the ratio of clauses per variable - $r = m/n$
- $m$ = number of clauses, $n$ = number of boolean variables
  ![](https://i.imgur.com/w0fbWDT.png)

- As you increase the ratio of clauses to boolean variables 
- As you increase $n$ (80), the no of variables, this curve seen becomes steeper