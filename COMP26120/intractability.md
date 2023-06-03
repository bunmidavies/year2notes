
### tractability/intractability
vid 1
- hardness = runtime. Establishing if a problem is too hard is important to decide whether estimation techniques should be used, and if it is worth the time properly solving
- solvable = given some inputs to a problem, a yes/no on whether a problem has a solution with those inputs is returned (the actual solution need not be necessarily returned)
- P = ==solvable in polynomial time by a deterministic machine== $O(n^c)$
- NP = ==verifiable in polynomial time / solvable in polynomial time by a non-deterministic machine==
- $P \subseteq NP$ - whether P is equal to NP or not is the ==P vs NP argument==
- NP-hard = ==at least as hard as all problems in NP==
- NP-complete = ==both NP and NP-hard (the intersection of the two classes)==
![](https://i.imgur.com/zxdih86.png)
- NP-complete lies at where the big blue line and orange line are lying, i.e. at the boundary
- ==reduction== = problem A and B, you know how to solve B - turn inputs of problem A to inputs of problem B, and solve problem B with these inputs, effectively solving A
- ==all problems are only decision problems==
vid 2
- formal definition of P
![](https://i.imgur.com/IdvZc3m.png)
- standard encoding of abstract inputs, to serialise anything, and only ever consider size rather than the actual content of the inputs
vid 3
- vertex cover example problem - can check if C is a solution in O(kn) i.e. checking every edge - thus verifiable in polynomial time
- therefore C is the ==polynomial-time verifiable certificate== for the problem
- all problems in NP have some certificate which you can use to verify a solution in polynomial time
![](https://i.imgur.com/DTV9ipK.png)
- SAT problems (2-SAT,3-SAT) are also NP problems
- task selection (decision)
- edit distance (decision)
- longest common subsequence (decision)
- formal NP definition (top one is verifiable in polynomial, bottom is solvable w/ non deterministic in polynomial)
> [!tip] 3-SAT vs 2-SAT
> simply put, $a \lor b \lor c$ can't be represented as 2 clauses. For this reason, 2-SAT is easier than 3-SAT, thus 3-SAT can't be reduced to 2-SAT. 2-SAT and 3-SAT are both reducible to SAT since SAT is just the generalisation

![](https://i.imgur.com/sMwcVZn.png)
![](https://i.imgur.com/aeqgw37.png)
- CO-NP (not really covered in this class)

> [!Note] Non-deterministic Machine
> A machine that is able to compute all possible paths in an algorithm simultaneously. This machine can solve problems in the NP class in polynomial time 

>[!faq] P = NP?
> Non-deterministic machines currently only exist as theoretical concepts within computational analysis. However, if non-deterministic machines were found to have a real life implementation, then this implies NP problems could also be solved in polynomial times, like P, implying P=NP

- ==nondeterministic machine== - able to compute all possible paths at the same time. can be thought as getting 'very lucky'. It can solve all NP problems in polynomial time - thus if it is found that a nondeterministic machine exists, then P must equal NP, and all problems in P/NP are solvable in polynomial time

vid 4
- there are many notions of reducibility - we focus on polytime mapping reducibility to show ==NP completeness==
- polytime mapping reducibility = polytime many-one reducibility, karp-reducibility

> [!info] Reducibility
> For two languages (problems) A and B, if we say A is reducible to B, it means that problem B can be used to solve problem A
> $$A\leq_p B$$
> $$\text{A is reducible to B}$$
> you can think of A being ==no harder== than B, and B being ==at least as hard== as A

- if A is hard, then B MUST also be hard

> [!info] Poly-time Mapping Reducibility
> Polynomial time mapping A is reducible to B ($A \leq_p B$) if there is a polynomial time function $f$ where $w \in A$ iff $f(w) \in B$
> $f$ itself is known as the reduction, and $w$ is the inputs to some problem
> ![](https://i.imgur.com/wnwFzuR.png)

- decision problems are never harder than optimisation problems

> [!info] NP-Completeness / NP-Hard
> A language (problem) $L$ is NP-Complete (NPC) if:
> 1. $L \in NP$
> 2. $L' \leq_p L$ for all $L' \in NP$
> The problem is NP, and at least as hard as all other NP problems, since all other NP problems can be reduced to it
> If (1) isn't satisfied, i.e. its not in NP itself, this problem is known as ==NP-Hard==

- nothing in NP is harder than an NPC problem - if you can solve NPC in polynomial time, this will also imply P = NP. In short, NPC problems are just the hardest problems in NP, which any problem in NP can be reduced to
- any NPC problem can be reduced to another NPC problem - showing the ==first NPC problem== is what the Cook-Levin Theorem addresses

### NP-Complete Problems
- note that all problems are phrased as decision problems as that is what we care about
- satisfiability, all to do with finding some assignment of boolean variables
>[!info] Circuit-SAT
>Given a (one-output) boolean combinational circuit C, is there an assignment that causes the circuit to be 1?

>[!info] SAT
>Given a boolean expression B over variables V, does there exist an assignment A of truth values to the variables V that makes B true?

>[!info] k-SAT
>Given a set B of k-clauses variables V, is there an assignment of truth values to the variables V that makes B true?

>[!info] Vertex Cover Problem
>Given a graph $G = (V,E)$ and an integer $k$, is there a subset $C\subseteq V$ such that $|C|\leq k$ and for every $(u,v) \in E$ either $u \in C$ or $v \in C$

> [!info] Clique Problem
> Given a graph $G = (V,E)$ and an integer $k$, is there a subset $C\subseteq V$ such that $|C|\geq k$ and for every $u,v\in C$ we have $(u,v)\in E$ or $(v,u)\in E$

>[!info] Graph Colouring Problem
>Given a graph $G = (V,E)$ and an integer $k$, is there a way to partition $V_1,...,V_k$ such that for every $u,v\in V_i$ we have $(u,v)\notin E$ and $(v,u) \notin E$

![](https://i.imgur.com/rBIxrx8.png)
3 different cliques highlighted in different colours (where every node is connected to eachother)

- some graph definitions which are used in the problem definitions
>[!tip] Path
>A path in a graph is a sequence of vertices $v_1,v_2,...,v_n$ such that $(v_i,v_{i+1})\in E$

>[!tip] Cycle
>A cycle is a *path* (see above) where $v_1 = v_n$

>[!tip] Hamiltonian Path
>A path with $v_1,v_2,...,v_n$ where $n=|V|$ (includes all vertices)

> [!tip] Simple Path
> A path is simple if each $v_i$ in $v_1,v_2,...v_n$ is distinct

> [!info] Hamiltonian Cycle Problem
> Given a graph $G = (V,E)$, does there exist a cycle that visits each vertex exactly once?

>[!info] Travelling Salesman Problem
>Given a weighted graph $G = (V,E,w)$ and an integer $k$, is there a Hamiltonian cycle whose weight is at most k?

- slight alterations to the above problems which result in problems which are in $P$
> [!info] Chinese Postman Problem
> Similar to the Travelling Salesman Problem, but concerned with covering all edges rather than just vertices. ==This problem is in P==

> [!info] Eulerian Cycle Problem
> Similar to the Hamiltonian Cycle Problem, but concerned with covering all edges rather than just vertices. ==This problem is in P==

> [!info] Longest Path
> Given a graph $G = (V,E)$, two vertices $u,v \in V$ and an integer $k$, is there a *simple* path (distinct vertices only) between $u$ and $v$ of ==at least== length $k$?

> [!info] Shortest Path - **NP, Not NP-Complete**
> Given a graph $G = (V,E)$, two vertices $u,v \in V$ and an integer $k$, is there a path between $u$ and $v$ of ==at most== length $k$?

- problems which are more popularised as optimisation problems
- the bin packing problem often includes multiple bins
> [!info] Bin Packing Problem (aka partition problem)
> Given a set $I$ of items, each with size $s(i)$ for $i\in I$, a bin with capacity $B$, and a positive integer $k$, is there a partition of $I$ into disjoint sets $I_1,...,I_k$ such that $\text{sum}(I_j) \leq B$?

> [!info] 0-1 Knapsack (aka subset sum)
> Given a set of $n$ items with weight $w_i$ and value $v_i$, a minimum value $V$, and a maximum weight $W$, is there a subset of items whose **total value** $\geq$ V, and **total weight** $\leq W$?

- linear programming decision problem, with integers instead of reals used earlier in the course
> [!info] Integer (Linear) Programming
> Given an objective function $z = x_1 + ... + x_n$ and a set of constraints of the form $a_ix_i + ... + a_kx_k \leq b$ and a positive integer $k$, is there an assignment of **positive integers** to $x_1,...x_n$ such that $z\geq k$

- integers = NP-complete, real numbers = P

### Turing Machine
Components of Turing Machine:
- Finite control contains operations of the machine
- Head
- Infinite read/write input tape
On an input $w$, a turing machine can:
1. accept $w$, entering an accept state
2. reject $w$, entering a reject state
3. reject $w$ (infinite loop - i.e. a halt state)
Formal definition is a 7-tuple
![](https://i.imgur.com/HmYcbFl.png)
- Non deterministic turing machines - can explore multiple paths simultaneously in a transition function (is able to solve NP problems in polynomial time)

### Representing Turing Machine Configuration
- keeps track of machine tape contents, current state and head location
- for instance, $abbq_3aca$ means the machine is currently in state $q_3$, and the head is on the character$a$

### Cooke-Levin Theorem
- works through proving that SAT is NP-Complete
	1. $\text{SAT}\in NP$ -> easy to verify if assignment results in true for SAT
	2. for each problem $A$ in $NP$, show that $A \leq_p \text{SAT}$:
		- build poly-time reduction from $A$ to $\text{SAT}$
		- reduction $f$ maps inputs of $A$ to a formula for $\text{SAT}$ - $\phi_{M,w}$
			- $M$ is the NTM that decides $A$ in polynomial time (hence NP)
			- $w$ is the input
		- the formula is only satisfiable for SAT when it is accepted in problem $A$ by the NTM which verifies input $w$

part 2 / 3 of cook-levin theorem
![](https://i.imgur.com/ZXPqdxX.png)
basically creating a formula which can be fed into SAT, which mimics the behaviour of how a non deterministic machine $M$ operates on inputs $w$
$\phi_{M,w}$ is satisfiable only when $M$ accepts $w$
we've therefore shown we have some arbitrary NP problem $A$, and have been able to reduce it to $\text{SAT}$ - the inputs to the problem $A$ are 

size of final formula -> $|\phi_{M,w}| = O(n^{2k})$