[[COMP26120]]

divide-and-conquer is a ==top-down== approach - this means breaking down the original problem you have into smaller problems

the opposite of this is ==bottom-up== - where smaller solutions are combined in order to gain a whole solution (this may seem similar to top-down, but in this case we already know what these smaller problems/solutions are, so there is no ==breaking down== process)

[[karatsuba multiplication]] is an example of applying a divide and conquer solution to a problem, reducing time complexity from $O(n^2)$

==memoization== is a technique which can be used within divide and conquer - it involves using a global data structure like a [[hash map]] perhaps, to store previous answers to calculations. Before calculating anything, check if it exists in the hash map (also known as a look up table), and if it does use this result

[[dynamic programming]] is similar to divide and conquer, in that it makes use of ==memoization== but it also typically solves problems with a ==bottom-up== approach

