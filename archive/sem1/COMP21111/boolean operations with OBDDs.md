[[COMP21111]]

the goal is to create an [[OBDD]] which represents the disjunction of some other OBDDs, which means that the OBDD we create represents the disjunction of the formulas the OBDDs represent:
![](https://i.imgur.com/ceqP9z7.png)


We do this by using a fundamental property of ==if-then-else==

f(if p then $l_1$ else $r_1$, ... , if p then $l_n$ else $r_n$) is ==equivalent== to:
if p then f($l_1...l_n$) else f$(r_1...r_n)$

This property allows us to apply $f$ to the subdags corresponding to $p = 0$ (the subdags beneath the dashed edge of $p$), giving us a dag $D_0$ 

there are two main functions covered: ==disjunction== and ==conjunction==

### disjunction algorithm

==procedure== `disjunction`$(n1,...,n_m)$
==parameters== global dag $D$
==input== nodes $n_1,...,n_m$ representing $F_1,...,F_m$ in global dag $D$
==output== a node $n$ representing $F_1\lor ... \lor F_m$ in (possibly modified) global dag $D$
**begin**
	if some $n_i$ is $1$ then ==return 1== //single 1 in disjunction returns true
	if $m = 0$ then return $0$
	if $m = 1$ then return $n_1$
	if some $n_i$ is $0$ then:
		return `disjunction`($n_1,...,n_{i-1},n_{i+1},...,n_m$) //disjunction of all nodes except $n_i$
	$p$ = `max_variable`($n_1,...,n_m$)
	for all $i = 1...m$
		if $n_i$ is labelled by $p$
			then $(l_i,r_i)$ = (neg($n_i$),pos($n_i$))
		else $(l_i,r_i)$ = ($n_i$,$n_i$)
	$k_1$ = `disjunction`($l_1,...,l_m$)
	$k_2$ = `disjunction`($r_2,...r_m$)
	return `integrate`($k_1$,$p$,$k_2$,$D$)
**end**

- $m=0$ means that we have no nodes, and the disjunction of no nodes is $0$
- similarly $m=1$ means there is only one node i.e. only one formula in our dag, so we just return that formula
- we remove $n_i$ from the disjunction because we know that if it is $0$, then it is of no use to us
- $neg$ and $pos$ represent the subdags we obtain by setting the parameter node to false and true, respectively - we only do this in the case where we are dealing with the ==max variable==, which is why we loop through all nodes and check if its the one we want

### conjunction algorithm

==procedure== `disjunction`$(n1,...,n_m)$
==parameters== global dag $D$
==input== nodes $n_1,...,n_m$ representing $F_1,...,F_m$ in global dag $D$
==output== a node $n$ representing $F_1\lor ... \lor F_m$ in (possibly modified) global dag $D$
**begin**
	if some $n_i$ is $0$ then ==return 0== //single 0 in conjunction returns false
	if $m = 0$ then return $1$
	if $m = 1$ then return $n_1$
	if some $n_i$ is $1$ then:
		return `conjunction`($n_1,...,n_{i-1},n_{i+1},...,n_m$) //conjunction of all nodes except $n_i$
	$p$ = `max_variable`($n_1,...,n_m$)
	for all $i = 1...m$
		if $n_i$ is labelled by $p$
			then $(l_i,r_i)$ = (neg($n_i$),pos($n_i$))
		else $(l_i,r_i)$ = ($n_i$,$n_i$)
	$k_1$ = `conjunction`($l_1,...,l_m$)
	$k_2$ = `conjunction`($r_2,...r_m$)
	return `integrate`($k_1$,$p$,$k_2$,$D$)
**end**