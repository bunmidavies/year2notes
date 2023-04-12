[[COMP21111]]
# Binary Decision Diagrams / Trees

## <span style="font-family:roman">Binary Decision Tree</span>
- A binary decision tree is a tree $d$ such that:
	1. the internal nodes of $d$ are labeled by variables
	2. the leaves of $d$ are either $0$ or $1$
	3. every internal node in $d$ has exactly two children, the two arcs from $d$ are dashed for $0$, and solid for $1$
	4. nodes on every path of $d$ have unique labels (i.e. the value of each variable is determined only once on a single path)

## <span style="font-family:roman"> If-Then-Else Normal Form</span>
- If-then-else normal form is inductively defined as:
	1. $\top$ and $\bot$ are formulas in if-then-else normal form
	2. if $F_1$ and $F_2$ are formulas in if-then-else normal form not containing occurences of variable $p$, then if $p$ then $F_1$ else $F_2$ is in if-then-else normal form
- Example: *if $p$ then $\bot$ else $\top$*  is if-then-else normal form for $\neg p$

## <span style="font-family:roman">Binary Decision Tree + If-Then-Else</span>
- Given a binary decision tree $d$, for every node $n$ in $d$ we inductively define a propositional formula $F_n$ as follows:
	1. if $n$ is $0$, then $F_n$ = $\bot$; if $n$ is 1, then $F_n$ = $\top$
	2. if $n$ is an internal node labeled by variable $p$, then:
	   $F_n$ = *if $p$ then $F_{pos(n)}$ else $F_{neg(n)}$*

## <span style="font-family:roman">Binary Decision Tree Formula</span>
```
procedure bdt(F)
input: prop. formula F
output: binary decision tree
parameters: function select_variable
begin
	F := simplify(F)
	if (F = 1) return 1
	if (F = 0) return 0
	p := select_variable(F)
	return binary tree(p,bdt(F(neg(p))),bdt(F(pos(p)))) 
```
![](https://i.imgur.com/7VJUCDj.png)


**Every formula has an if-then-else normal form**

## <span style="font-family:roman">Binary Decision Diagrams</span>
- Binary decision diagrams eliminate two common redundancies that exist within regular binary decision trees
- A Binary Decision Diagram is a **directed acyclic graph** (dag) $d$ that satifies the properties of a binary decision tree plus the following:
	1. for every node $n$, its left and right subgraphs are different to eachother
	2. every pair of subdags of $d$ rooted at two different nodes $n_1$ and $n_2$ are non-isomorphic

- to eliminate the redundancies within any given dag, the following transformations must be performed:
	1. if there exists a node $n$ such that $neg(n)$ and $pos(n)$ are the same dag, then remove the entire node
	2. if the subdags rooted at two different nodes $n_1$ and $n_2$ are isomorphic, then merge into one

- BDDs allow you to check validity / satisfiability in constant time, and the size of a BDD for a formula is exponential to the size of that formula
- There still remains two problems for BDDs:
	1. how to implement equivalence checking efficiently
	2. how to implement some boolean operations, e.g. conjunction

## <span style="font-family:roman">Ordered BDDs</span>
- let $\gt$ be a linear order on variables and $d$ be a BDD. $d$ respects $\gt$, if for every node $n_1$ labeled by a variable $p_1$ and its child $n_2$ labeled with $p2$, $p1 \gt p2$
- a BDD is **ordered** if it respects some order

## <span style="font-family:roman">OBDD algorithm</span>
![](https://i.imgur.com/hGKw6kL.png)