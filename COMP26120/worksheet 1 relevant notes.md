***
## 2.1 - insertion sort + invariant explanation

- Insertion sort basically just works by having what is supposed to be the sorted list being stored somewhere separate, and item by item, looping through the array until you find its correct position
- **loop invariants** - loop invariants are used to show why an algorithm is correct. Three things need to be shown with a loop invariant:
	- Initialisation: invariant is true before the loop even starts (**base case**)
	- Maintenance: if invariant is true before iteration of a loop, it must be true before the next iteration (**step case**)
	- Termination: when the loop finally terminates (after last iteration), the invariant gives a property to show that the algorithm is correct


- a loop invariant proof is a form of induction i.e. in order to prove that a property holds, you use a base case and an inductive step (the first 2 properties from above)

### loop invariant example: insertion sort

- before the insertion sort begins, you start with the sorted subarray just containing the first element of the array to be sorted. Because this array only contains one element, it must be sorted, so our condition of the res list being sorted is true
- we say that while the loop runs for now, the fact that $i$ gets incremented with each iteration preserves the loop invariant
- once the loop terminates, $i$ will be equal to $n+1$, where $n$ is the size of the original array. The resultant array being sorted proves that the algorithm is correct

[pages 20/21/22 go through pseudocode syntax]

## 2.2 - analysing algorithms

- supposedly not what the worksheet is based on, so leaving for now until further notice for the most part

- worst case running time gives an upper bound on running time for any input
- $\Theta$ / big O in the algorithms book essentially means *roughly proportional when $n$ is large* - this is later formally defined in chapter 3
- From what I understand, the difference between O-notation and $\Theta$ when they're shown in the book, is that O-notation is actually just an upper bound with no limit, so you could technically give an O-notation which is way higher than the actual algorithm, and its still valid.
- $\Theta$ is the *tight bound* on the behaviour of a function, thus it lies within O and $\Omega$ (the lower bound, which can be as low as you want as well)

## 2.3 - designing algorithms

- insertion sort was an incremental method, but this chapter introduce divide-and-conquer, through a classic example of merge sort
- example shown is basically identical to lecture video

- when an algorithm contains a recursive call, you can describe the running time by a *recurrence equation / recurrence* - this describes the overall running time on a problem of size $n$, using the running time of the *same algorithm on smaller inputs*
- using this recurrence, you can solve it in order to provide actual bounds ($\Theta$) on the algorithm

- $T(n)$ is typically described as the worst case running time for a problem of size $n$

### Setting up a recurrence for merge sort

- $T(n)$ is the worst case running time of merge sort, given $n$ numbers
- Dividing takes constant time (dividing list in half), so $D(n)$ = $\Theta(1)$
- When you have divided the problem, you now have the same problem but of size $n/2$, and 2x the problems you originally had. So it makes sense to say that each division adds $2T(n/2)$ to the runtime
- Combining (Merging) all the subproblems takes $\Theta(n)$ time, and this subalgorithm can be referred to as $C$

- Therefore, if we have a problem which is $T(n)$, and we've gone through the runtimes for the different steps within the problem (merge + recombine), we get:

$$T(n) = 2T(n/2) + \Theta(n)$$

# 4

- When a recurrence uses inequalities, we should be expressing the solution after solving it in terms of the relevant notation, e.g.:
- $T(n) \leq 2T(n/2) + \Theta(n)$ 
- We use $O$-notation, as we have just stated an upper bound (not a tight bound which would be $=$)
- $T(n) \geq 2T(n/2) + \Theta(n)$
- We use $\Omega$-notation, as we have just stated a lower bound

- It is possible to divide problems in a recurrence not only in half, but in irregular ways as well, for instance
- $T(n) = T(n/3) + T(2n/3) + \Theta(n)$
- This turns out to have solution $T(n) = \Theta(nlogn)$
- Another common example of this are algrithms which solve subproblems with one less element, for instance
- $T(n) = T(n-1) + \Theta(1)$
- Which gives solution $T(n)=\Theta(n)$

- There are a number of methods for solving recurrences, but the course is mainly concerned with the following:
	- Substitution method - guessing the form of a bound, then using induction to prove the guess, and solve for constants
	- Recursion tree method - models recurrence using a tree, determining costs at each level/node and adding everything up
	- Master method - works for recurrences which look like $T(n) = aT(n/b) + f(n)$ where $a > 0$, $b > 1$, and $f(n)$ is a given "driving" function (?)
- The master method is common because divide-and-conquer algorithms typically create $a$ subproblems, each of which being $1/b$ of the size of the original problem, and $f(n)$ is used to represent the time to divide and combine the subproblems (not recursive?)

### substitution method (4.3)

- the substitution method has 2 main steps:
	1. Guess the form of the solution using symbolic constants
	2. Use induction to show that the solution works, then find the constants
- The guessed solution is substituted for the function on smaller values, which is where the 'substitution' name comes from
- The substitution method is recommended for establishing an upper  (O) or lower ($\Omega$) bound on a recurrence, which can then be combined to give a $\Theta$ bound

- **Example of the substitution method** 
- we will determine an upper bound on the recurrence equation:
  $T(n) = 2T(n/2) + \Theta(n)$
- We will guess that the upper bound is the same as a similar algorithm in the book. So $T(n) = O(nlogn)$ - now the substitution method can be used once a guess has been made
- Our inductive hypothesis is that $T(n) \leq cnlogn$ for all $n\geq n_0$ ($T(n)$ is $\leq$ because we're only solving for upper bound), where $c>0$ and $n_0 > 0$ can be defined later
- If the inductive hypothesis can be established, then we can concluced that $T(n) = O(nlogn)$. But that isn't used in the inductive hypothesis because we don't know what constants might bet introduced
- We assume by induction that the upper bound we wrote holds for all numbers as big as $n_0$, and less than $n$
- So if $n\geq 2n_0$, our bound holds for $n/2$, so $T(n/2)\leq c((n/2)log(n/2))$ (we just replace all $n$ with $n/2$)
- So now we sub this in for $T(n)$, and use basic algebra/logs:
- $T(n) \leq 2(c(n/2)log(n/2)) + \Theta(n)$ (note that $\Theta(n)$ is our "driving" function)
- $T(n) \leq cn log(n/2)$ (omitting the $\Theta(n)$ for now cos im lazy)
- $T(n) \leq cn(logn - log2)$
- $T(n) \leq cn(logn - 1)$ (logs are in base 2)
- $T(n) \leq cnlogn - cn$
- Therefore $T(n) \leq cnlogn - cn + \Theta(n)$, but because we drop non dominant terms we end up with $T(n) \leq cnlogn$
- **This matches up with our inductive hypothesis**
- In our proof we also need to handle the base case

- I think parts of the method can get confusing given that there is $n$, $n_0$, $n'_0$, but the last sentence kind of sums it up: *You ground the induction on a range of values from a positive constant $n_0$ up to some constant $n'_0 > n_0$, such that for $n \geq n'_0$, the recurrence always bottoms out to a constant sized base case between $n_0$ and $n'_0$s

## 4.5 - Master Method for solving recurrences

- The master method is designed for recurrences in the form:
  $$T(n) = aT(n/b) + f(n)$$
  Where $a > 0$, $b > 1$, and both are constants
- $f(n)$ is the driving function (divides and combines the subproblems once solved)

- The **master theorem** has 3 cases which determine the asymptotic behaviour of $T(n)$
	1. If there is a constant $\epsilon > 0$ such that $f(n) = O(n^{log_b{a-\epsilon}})$, $T(n) = \Theta(n^{log_b{a}})$
	2. If there is a constant $k \geq 0$ such that $f(n) = \Theta(n^{log_b{a}}\cdot log_k{n})$, $T(n) = \Theta(n^{log_b{a}} \cdot log_{k+1}n)$ 
	3. If there is a constant $\epsilon > 0$ such that $f(n) = \Omega(n^{log_b{a+\epsilon}})$, and if $f(n)$ additionally satisfies the *regularity condition* $af(n/b)\leq cf(n)$ for some constant $c < 1$ (and all sufficiently large $n$), then $T(n)=\Theta(f(n))$

- $n^{log_b{a}}$ is called the *watershed function*
- In order to determine these cases, you notice that you are typically comparing the driving function $f(n)$ to the *watershed function*