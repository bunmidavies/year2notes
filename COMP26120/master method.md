[[COMP26120]]

the master method is used to solve recurrence equations, but typically only for ==divide and conquer== algorithms (i.e. an algorithm that divides a problem of size $n$ into subproblems, each of size $n/b$)

With divide and conquer problems, the work can be split into two functions:
- $D(n)$ - the work to ==divide== the problem into subproblems
- $C(n)$ - the work to ==combine== the solved subproblems

Thus, recurrences solvable via the master method take the form:
$$T(n) = aT(n/b) + f(n)$$
Where $a \geq 1, b > 1$ and $f$ is ==asymptotically positive==

we say that subproblems of size $n/b$ are each ==solved== in $T(n/b)$, and $f(n)$ is the cost to ==divide the problem and combine the results==

the rules are as follows:
![](https://i.imgur.com/EfcjHq9.png)

refer to [[asymptotic notation]] to understand the 3rd rule of the master method

### Example
we want to know the complexity of the following
$$T(n) = 2T(n/2) + \Theta(n)$$
using what we defined above, we know that:
- $a$ = 2
- $b$ = 2
- $f(n) = \Theta(n)$

using this info, we want to figure out which version of the master method we use

we see that
$$log_ba = log_22 = 1$$
therefore
$$n^{log_ba} = n^1 = n$$
so we can say that
$$f(n) = \Theta(n^{log_ba})$$
and this is the ==2nd version of the master method==

This means $T(n) = \Theta(n^{log_ba}logn)$

So our ==final answer is== $T(n) = \Theta(nlogn)$
