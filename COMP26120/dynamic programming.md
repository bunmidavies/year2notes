[[COMP26120]]

dynamic programming is part of the problem decomposition technique within [[algorithmic techniques]], similar to [[divide and conquer]]

in dynamic programming, we ==already know what the subproblems are==, so we build up the entire solution using subproblems

an example of this is using ==previous answers== in the ==fibonacci sequence== to calculate the next number in the sequence:
$$fib[i] = ans[i-1] + ans[i-2]$$
where $ans$ is a structure/map storing these previous answers

the structures in dp problems are typically either ==1-dimensional== or ==2-dimensional==

### requirements for dp / divide and conquer

1. ==simple/similar subproblems== - being able to break down the problems into common subproblems with the same structure
2. ==optimality when combining== - optimal solutions to subproblems should be able to be combined to produce a global optimal solution

in the final video of the 12th week, an [[edit distance algorithm example]] is shown as a 2nd example of dynamic programming
