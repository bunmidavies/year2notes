[[COMP24011]]
# Week 3
- Constraint satisfaction, and how to solve such problems


## What are constraint satisfaction problems?

- Example problem:
```
Each student picks 5 courses to take in sem1, between:
	COMP21111, COMP22111, ..., COMP24011
Activities for COMP24011 includes:
	COMP24011_lecture, COMP24011_lab
COMP24011_lab has a number of groups:
	COMP24011_lab_F, COMP24011_lab_G, COMP24011_lab_H
240+ students will not fit into one lab group

Timetable sessions for COMP24011_lab_H:
	Week4.tue. 9am-11am
	Week6.tue. 9am-11am
	Week8.tue. 9am-11am
	Week10.tue. 9am-11am

How do you put the students in groups such that:
	There are no timetable clashes
	There are no capacity violations

Constraints:
	Students must have time for lunch
	Group sizes should be even
```

- Constraint network example following original example:
- Suppose a student is taking COMP21111, COMP21044:
	the **variables** are: $x_{COMP21111.ex},x_{COMP21044.lab}$
	the **domain** of $x_{COMP21044.lab} =$ {COMP24011_lab_F, COMP24011_lab_G, COMP24011_lab_H} 
	the **constraints** = the activities which have a clash (e.g. examples classes for group F and lab for group G are both at 9am tuesday). Therefore, the 2 activites **will not be in the relation**

- Better example: K-colouring
	- Varibles are vertices: $v_1,...,v_n$
	- $D_i = {1,2,3}$ for all $i$
	- Constraints = relations $R_{i,j}(v_i,v_j)$ for $(v_i,v_j)\in E$:
	  $R_{i,j}(v_i,v_j) = {\langle 1,2\rangle \langle 1,3\rangle \langle 2,1\rangle \langle 2,3\rangle \langle 3,1 \rangle \langle 3,2\rangle}$ (i.e. all possible combos from vertex to vertex is just given as a list)

- Should be noted that constraint satisfaction problems are also known as **commutative** - the order in which values are assigned to variables doesn't actually matter

## How are constraint satisfaction problems solved?

## Constraint propagation

- **The constraint propagation video (Week 3 Pt. 2) is about 40 minutes long and the topic is supposedly huge anyways, so as of 09/10/2022 the following notes are only be based off Sections 6.1, 6.2, 6.3, 6.5 in Artificial Intelligence: A Modern Approach**

- In constraint satisfaction problems, there are basically two choices - an algorithm can search (backtracking etc.), or do a type of **inference** called **constraint propagation** - using the constraints to reduce the number of values a variable can take, causing a kind of domino effect for other variables
- The search and propagation could also be combined
- The key to constraint propagation is **local consistency** - if each variable is treated like a node in a graph, and each binary constraint is an arc, then forcing local consistency within this graph would remove invalid values

- **Node consistency** - a variable is node-consistent if all possible values that the variable can take satisfies its unary constraints (i.e. none of the values it can take are illegal).
- A network is node-consistent if all variables within it have node-consistency. *It's common for constraint satisfaction problem solvers to convert n-ary constraints into binary constraints, then enforce node consistency everywhere thus resulting in a solution*

- **Arc-consistency** - a variable is arc-consistent if every value in its domain satisfies the binary constraints. Therefore the definition is more like, variable x is arc-consistent with variable y if all possible combinations of x and y are related in the constraint defined for (x,y)
- Therefore a network is arc-consistent if every variable is arc-consistent with every other variable
- Arc consistency can be extended to n-ary constraints rather than just binary, and this is usually called **generalized-arc-consistency** or **hyperarc consistency**

- The main problem with arc consistency is as follows: Arc consistency may find that every variable is arc consistent, but in map colouring problems where only 2 colours are available, but technically 3 are needed, arc consistency won't be aware of this problem, it just finds that there are no illegal values within the domains of variables
- **Path consistency** tightens binary constraints by using implicit constraints that are created by looking at triples of variables, for instance:
	- The set {Xi, Xj} is path consistent with Xm if for each assignment {Xi = a, Xj = b}, there exists an Xm which satisfies the constraints on {Xi, Xm} and {Xm, xj}
- This has basically introduced a third variable in between i and j, and is stricter on problems with binary constraints, and can figure it out if no actual solution exists for these kinds of problems
- This can then be extended with the notion of **k-consistency** - 

- **Global constraints** - a global constraint is a constraint which involves an arbitrary number of variables. They occur much more frequently in real problems
- The basic way of checking whether global constraints are satisfied is if there are more variables in the problem than there are possible values in the constraint. If this is the case then you know there cannot be a possible solution

- **Resource constraint / Atmost constraint** = in problems where the sum or some kind of maximum exists for the values being assigned across all variables
- For instance in a schedulling / assignment problem, where 4 tasks are to be solved, and between 3 and 6 people can be assigned to a single task. If there was a resource constraint of no more than **10** people being assigned in total, you find that even if assigning the min. number of people to tasks (3), 3 x 4 > 10 so there is no possible solution

- For bigger problems, large sets of integers become less appropriate, such that another method of **bounds propagation** becomes used
- We describe a problem as **bounds consistent** if for every possible variable, within its bounds there exists a value (within bounds) of another variable which satisfies the constraint between those two variables. If a problem isn't bounds consistent then it cannot be solved


## Backjumping / Backtracking

- As mentioned at the start of the previous section, solutions to constraint satisfaction problems can either be inferred (above) or searched (now). A fair amount of the time it is actually the case that inferrence alone doesn't solve a problem, so searching must be used
- The backtracking search is a DFS which chooses values for variables, one at a time, then **unchooses** these values if no more values can be assigned  (regardless if whether a solution is found or not) - the algorithm itself will store one state which it repeatedly alters
- Backtracking searches do not require heuristic functions / domain specific knowledge in order to improve efficiency, but questions such as:
	1. Which variable should be assigned next, and in which order should these be tried?
	2. Which inferences should be performed at each step?
	3. If the search reaches an assignment which violates a constraint, can the search avoid doing this again?
- The answers / following improvements are as follows:
1. **minimum-remaining-values** heuristic is an approach where the variable with the least possible values to choose from is always selected as the next variable to assign a value to within the backtracking search. It means it may often pick the variable which is most likely to fail, and eliminate this error quickly (hence an alternative name of 'fail-first' heuristic). The **degree heuristic** is useful in deciding the very first variable - it picks the variable which is involved in the most constraints
2. **Forward checking** - after assigning a value to a variable, you eliminate any values for other variables which would go against arc consistency, and backtrack immediately if the domain of an unassigned variable has become empty - this can prune a number of branches from being traversed, thus improving efficiency
   
   However, forward checking doesn't look forward enough to see if variables other than the variable which has just been picked are arc-consistent. **MAC** (Maintaining Arc Consistency) detects inconsistencies across all variables
3. **Backjumping** - chronological backtracking is what backtracking algorithms will typically do. After a choice fails, go back to the same decision and choose something else. Instead, backtracking to a variable which might fix the problem encountered can work better. Backjumping will keep a **conflict set** for a certain decision, and backtrack to the most recent assignment in the conflict set.
   
   Backjumping is technically redundant if **forward-checking** is implemented, because such decisions which backjumping would act on will never be reached if forward-checking already prunes these decisions
   
   The general gist of backjumping is to backtrack based on the reason of failure, rather than simply backtracking when faced with failure

- **Conflict directed backjumping** is another process which addresses problems within backjumping, and aims to solve them by calculating another conflict set
- **Constraint learning** is the process of finding a minimum set of variables from a generated conflict set which causes a problem
- A **no-good** is a set of variable assignments which from that point on has been found to cause an inconsistency, thus has no purpose to be searched further

## R + N 6.5 Notes - The Structure of Problems

- This section examines how the structure of a problem can be used to find solutions quickly - it applies more to non constraint satisfaction problems
- If a constraint satisfaction problem has a graph in which every node only connects to two other nodes, we can actually model this as a tree
- To solve a tree structured constraint problem, firstly pick any variable to be the root of the tree. Then create an ordering such that each variable appears after its parent. This is a **topological sort**.
- Once this has been done, our tree is arc-consistent by definition so we just go down the tree and use whichever values are left. Thus **no backtracking is needed**

- So as explained above, if we reduce a constraint graph into a tree, we can actually traverse it like a normal tree and find a solution easily. So we want to see if there is a method to reducing trees

### Reducing graphs into trees
**Removing Nodes (Cutset Conditioning)**
- Removing nodes involves assigning values to some variables so that the remaining variables forms a tree
![](https://i.imgur.com/CobtHyb.png)

- In the given example, by removing $SA$, the graph becomes a tree. But how have we been allowed to remove $SA$? By picking a value for $SA$, removing $SA$ then removing all values from any other variable domains which would cause inconsistencies, we can effectively act like $SA$ doesn't exist for the rest of the graph
- The wrong value could obviously be chosen, so there is a general algorithm:
	1. Pick a subset $S$ of the CSP's variables such that you are left with a tree by removing $S$. $S$ is known as a **cycle cutset**
	2. For each possible assignment to the variables of $S$ that satisfy all the constraints in $S$ - Remove values from the domains of the remaining variables which cause inconsistencies with $S$'s assignments
	3. If the remaining graph (without cycle cutset) has a soltuion, return it alongside $S$'s assignments

**Tree Decomposition (Divide-and-Conquer)**
- Tree decomposition involves generating a set of connected subproblems based off the constraint graph. Each subproblem is solved independently, and the solutions are combined 
- Tree decompositions have the following requirements:
	1. Every variable from the original problem appears in at least one subproblem
	2. Two variables connected by a constraint from the original problem must appear together (with the constraint) in at least one of the subproblems
	3. A variable which appears in two subproblems must appear in all subproblems along the path connecting those subproblems
- The first two exist to make sure everything is included within the subproblems combined. The third exists to make sure every variable has the same value across subproblems if it happens to occur in multiple subproblems
- If one subproblem has no solution, the whole problem has no solution!
![](https://i.imgur.com/EPmWqRN.png)

- **Value symmetry** is where a solution which involves variable assignments can technically be rearranged to form another solution. Symmetry-breaking constraints can stop this, and the reason we may want this is to reduce the search space, improving efficiency and reducing complexity
- It's **NP-hard** to eliminate all symmetry among intermediate sets of values during search, but breaking value symmetry is an important concept which can be effective on a wide range of problems