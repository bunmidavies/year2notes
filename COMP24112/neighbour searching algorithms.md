[[COMP24112]]

studying efficient ways to compute nearest neighbours is an active research area in machine learning

the ==naive approach== to neighbour searching is by brute-force computing the distances between all pairs of samples and sorted neighbours

==tree-based== methods are examples of methods which follow a basic idea:
- it is known that A is very distant from B
- it is known that B is very close to C
- therefore, what is the relationship between A and C?
  A and C are ==very distant==, without any calculation.

this logic can be used to reduce the number of distance calculations which need to be computed