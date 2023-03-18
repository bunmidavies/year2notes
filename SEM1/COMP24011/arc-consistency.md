[[COMP24011]] - [[constraint propagation]]

the benefits/purpose of arc-consistency are described within [[constraint propagation]]

suppose there is constraint $R_{i,j}$, value $a \in D_i$, but there is no $b \in D_j$, such that $(a,b)\in R_{i,j}$

this basically means there is ==no value== in $D_j$ which can satisfy $R_{i,j}$ when $a$ is involved. This means $a$ in $D_i$ serves no purpose, and can be ==deleted== from $D_i$

==arc-consistency== describes a constraint network where for any $i$, $a \in D_i$ and $j$ such that $R_{i,j}\in C$, there is ==at least 1 element== $b\in D_j$ such that $(a,b)\in R_{i,j}$

this just basically means there are no values in any domain which is a 'no hoper', i.e. cant be paired up with any other value for all other domains

the ==algorithm== to ensure ==arc-consistency== is as follows:

AC-1($\bar{x}, \bar{D}, \mathcal{C}$)
	repeat until no changes
		for all $i,j$ such that $R_{i,j}\in \mathcal{C}$
			revise($i,j$)
			revise($j,i$)

where `revise(i,j)` is
$D_i := D_i \cap \pi_1(R_{i,j};D_j)$

### ac-3 (more efficient than ac-1)
![](https://i.imgur.com/mJREs9l.png)


==directional arc-consistency== ensures arc consistency for all $i \lt j$, rather than all $i$ and $j$

