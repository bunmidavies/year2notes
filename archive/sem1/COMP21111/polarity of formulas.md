**Polarity** - There are 3 types of polarity - Positive, Negative, Neutral. The main rules are as follows:
	- pol($A,\epsilon$) = 1
	- Let $A|_\pi = B$
		- if $B$ is made up of conjunctions or disjunctions, for all $B_i .. B_n$, pol($A,\pi.i$) = pol($A,\pi$)
		- if $B$ is $\neg B$, and $B$ has the position $\pi.1$, pol($A,\pi.1$) = $-$pol($A,\pi$)
		- if $B$ is $B_1 \rightarrow B_2$, so $\pi.1$ and $\pi.2$ are positions in $A$, pol($A,\pi.1$) = $-$pol($A,\pi$), **but** pol($A,\pi.2$) = pol($A,\pi$) [because implication is monotonic on second argument]
		- if $B$ is $B_1 \leftrightarrow B_2$, so $\pi.1$ and $\pi.2$ are positions in $A$, pol($A,\pi.i$) = 0 for all i [because double implication isnt monotonic or anti-monotonic for either argument]