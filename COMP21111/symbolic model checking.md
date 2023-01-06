[[COMP21111]]

there are a number of [[safety requirements]] that can exist within linear temporal logic ([[LTL]])

when designing a system, we would like to ensure all safety requirements are satisfied - this problem can be treated as a mathematical problem

a system can either be:
- represented as a ==state transition system== using:
	a. explicit representation (graph)
	b. symbolic representation (formal)
- express the ==desired properties== of the system in temporal logic

this leads us onto the [[symbolic model checking problem]]

==reachability== property = $\Diamond F$
==safety== property = $\square F$

given a transition system $\mathbb{S}$ with the transition relation $T$, we write $s_0 \rightarrow s_1$ given that the transition $(s_0,s_1)\in T$

therefore the formula $\Diamond F$ ==holds== on some computation path if and only if there exists an initial state $s_0$ and a state $s$ such that $s\models F$ and $s$ is ==reachable== from $s_0$

[[reachability]]