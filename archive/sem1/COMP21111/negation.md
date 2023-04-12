[[COMP21111]]
### comp21111 q4 - obdd negation algorithm

**procedure** *negation($n$)*
**parameters**: global dag $D$
**input**: a node $n$ representing $F$ in $D$
**output**: a node representing $\neg F$ in (modified) $D$
**begin**
	if $n$ is [1] then **return** [0]
	if $n$ is [0] then **return** [1]
	$p$ = max_var($n$)
	$(l,r)$ = $(neg(n),pos(n))$
	$l\_neg$ = negation($l$)
	$r\_neg$ = negation($r$)
	**return** integrate$(l\_neg,p,r\_max)$
**end**