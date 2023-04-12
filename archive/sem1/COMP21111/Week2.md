# Propositional Satisfiability Problem
- Given a propositional formula $A$, we want to check whether it is satisfiable or unsatisfiable
- If $A$ is satisfiable, we want to find a satisfying assignment for $A$ (A model of $A$)
- It's the first ever problem to be proved **NP-Complete**
- Propositional logic can be applied to many problems, one including the russian spy problem shown in the first video, or circuit equivalence (also shown in the first video)

# Satisfiability algorithms
- The main difference between evaluation algorithms and satisfiability algorithms using a truth table is that with evaluation algorithms we are just trying to find the result of a certain interpretation, meanwhile for satisfiability we are trying to find  a model of the propositional formula (an interpretation which satisfies the formula)
- The major drawback once again of all truth tables is scaling - we can try and solve this formula by using a compact truth table, which allows you to explore all possible values of the formula, without exploring all possible values of the propositional variables
- The key to satisfiability algorithms is guessing variable values and propagation


# 

# Monotonicity, position, polarity
- the order < is defined using 0 < 1
- a function is monotonic on its Kth argument if $a_k \leq a'_k$ $f(a_1...a_k...a_n) \leq f(a_1...a'_k...a_n)$. What this basically means that by changing the boolean value of $a_k$ from 0 to 1, the function can only keep the same value or increase, but NOT go down
- the oposite of this is **anti-monotonic**. Where if you decrease the value of the Kth argument, the value of the function decreases (or stays the same)
- $\land$ and $\lor$ are monotonic on all their arguments - if you increase an argument, the value of the connectives can only stay the same or increase
- $\neg$ is **anti-monotonic** (by increasing the value that is being negated, you decrease the output from the function)
- $\rightarrow$ is monotonic on its second argument, but anti-monotonic on its first argument
- $\leftrightarrow$ is neither monotonic or anti-monotonic on either arguments

- Positions are used to defined subformulas within a formula
- We can define positions by numbering connectives in a formula in order, then using a number path down a parse tree to refer to parts of the formula
![](https://i.imgur.com/SdBIcNZ.png)


- The formal definition for a position is as follows:
  A **Position** is a sequence of any positive integers $a_1 .. a_n$ where $n\geq 0$, written as $a_1 . a_2 ... a_n$
  The empty position is denoted by $\epsilon$ when n = 0
  The position in formula $A$ is denoted $A|_{position}$

- Every formula has a position $\epsilon$, which is just the formula itself

- [[polarity of formulas]]

- Colouring method to determine polarity for all positions:
![Uploading file...eig4x]()


- For conjunction / disjunction you do not colour the line blue nor red.
- Note that once reaching a 0 in the tree, you'll never get any value other than 0. This is because +0 and -0 are both equal to 0

# Monotonic replacement / pure atom rule

- As stated in [[propositional logic semantics]] $A[B]$ denoted that $B$ was a subformula of $A$
- Now, $A[B]_\pi$ can be used to denote that $B$ is a subformula of $A$ at position $\pi$
- For any interpretation $I$:
	  $I(A) \leq I(B)$ if and only $I \vDash A \rightarrow B$
- Reminder that $\vDash$ denotes model, aka $I$ satisfies $A\rightarrow B$


- **Equivalent Replacement Lemma** - if $I \vDash B \leftrightarrow B'$ then $I \vDash A[B] \leftrightarrow A[B']$
- Basically meaning if $B$ and $B'$ are the same in an interpretation, you can just replace $B$ with $B'$ and the value will stay the same

- **Monotonic Replacement Lemma** 
	- if pol($A,\pi$) = 1 and $I\vDash B\rightarrow B'$ 
	- then $I \vDash A[B]_\pi \rightarrow A[B']_\pi$ 
	- Basically meaning if the interpretation of $B'$ is greater than or equal to interpretation of $B$ then $I(A[B']_\pi)$ is greater than or equal to $I(A[B]_\pi)$. Therefore for formulas with positive polarity, then the formula is monotonic
	- if pol($A,\pi$) = -1 and $I\vDash B'\rightarrow B$
	- then $I \vDash A[B]_\pi \rightarrow A[B']_\pi$ 

- **Pure atom** - An atom (propositional variable) is pure in a certain formula, given that all occurences of it are positive, or all are negative (in terms of polarity). You can once again determine this using colouring method within parse trees
- **Pure atom theorem** - An atom *p* having only positive occurences in $A$ implies $A$ is satisfiable if and only if so is $A^\top_p$
	- When all occurences are negative = Replace with $\bot$
	- When all occurences are positive = Replace with $\top$
- This can be proved by applying the **monotonic replacement theorem**
- This theorem allows you to replace certain variables with $\top$ / $\bot$, and still satisfy interpretations as you would with the variables included