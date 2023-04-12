[[COMP21111]]

[[bounded model checking aka onesided forward reachability]] is good for finding bugs and unsafe states being reachable within a system, but cannot be used to ==fully show== that a system is fully ==safe== - this is because the algorithm doesn't terminate 

the algorithm builds on the idea of reachability within $n$ states, but relaxes it to $\leq n$ states

![](https://i.imgur.com/K5Q2C8l.png)


$S_n$ is used to denote all states reachable in $\leq n$ steps

this means $S_i \subseteq S_{i+1}$ for all $i$ (the set can ==only grow==)
the system must have a finite number of states, and from some point we reach a ==fixed state== (there exists a $k$ such that $S_k = S_{k+1}$)

#### algorithm

==procedure== CFReach(I, T, F)
==input== formulas I, T, F
==output== "yes" if reachable, "no" otherwise
begin
	i := 0;
	$R_{\leq 0}(\bar{x}) := I(\bar{x});$
	loop
		if $R_{\leq i}(\bar{x})\land F(\bar{x})$ is satisfiable then return "yes";
		else: $R_{\leq i+1}(\bar{x}) := R_{\leq i}(\bar{x}) \land \exists \bar{x}_i \land T(\bar{x}_i,\bar{x}));$		
		if $R_{\leq i}(\bar{x}) = R_{\leq i+1}(\bar{x})$ then return "no";
		i += 1
	end loop
end

this algorithm makes use of:
- conjunction/disjunction
- quantification
- satisfiability checking
- equivalence checking
therefore, the suitable implementation for this involves [[OBDD]]s and algorithms related to OBDDs