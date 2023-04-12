[[COMP21111]]

the main disadvantage of forward reachability algorithms (i.e. [[bounded model checking aka onesided forward reachability]] and [[complete forward reachability]]), is that they are not ==goal oriented== - they behave in the same way regardless of what the final states actually are

==backward reachability algorithms apply the transition relation backwards==

![](https://i.imgur.com/uxYogGV.png)


for example, if you were to use a ==forward reachability== algorithm on this graph, you would start from $s_0$, then work your way around the whole graph to find that you can't reach the bad state. Meanwhile, if you started from the ==bad state==, then you would notice that the initial state is not reachable ==much sooner==

#### algorithm

procedure BReach(I,T,F)
==input== formulas I, T, F
==output== "yes" or "no"
==begin==
	i := 0;
	$BR_{\leq 0}(\bar{x}) := F(\bar{x});$
	loop
		if $BR_{\leq i}(\bar{x}) \land I(\bar(x))$ is satisfiable then ==return "yes"==
		else: $BR_{\leq i+1}(\bar{x}) := BR_{\leq i}(\bar{x}) \lor \exists \bar{x}_i(BR_{\leq i}(\bar{x}) \land T(\bar{x},\bar{x}_i));$		
		if $BR_{\leq i}(\bar{x}) = BR_{\leq i+1}(\bar{x})$ then return "no";
		i += 1
	end loop
end