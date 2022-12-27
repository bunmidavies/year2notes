[[COMP26120]]

greedy algorithms are part of the [[solution space view]] for [[algorithmic techniques]]

a greedy algorithm always makes the ==best local choice==, this means while searching, all possible children are inspected, and the ==best== choice at this point of time is *always* picked

this means that greedy algorithms ==will NOT always find the optimal solution==. It never backtracks

greedy algorithms should be applied when we can make a series of choice such that we never need to go back and change our choice later

==task scheduling== is a common example of a problem which can be solved with a greedy algorithm

the ==exchange argument== can be used to prove that the greedy algorithm for the task scheduling problem finds not only *a solution* but the ==optimal== solution