[[COMP21111]] **only considers finite-state transition systems**

following on from how to formally define [[state changing systems]]

a transition system is used. it is a tuple consisting of:
	- $S$ - finite non empty set, containing all possible **states**
	- $In$ - a non empty subset of $S$, containing all **initial states**
	- $T$ - the transition relation. the set of pairs of states, which defines which states you can travel between (thus the pairs are all $S \times S$)
	- $\mathcal{X}$ - a set of state variables
	- $dom$ - the mapping from $\mathcal{X}$ to their corresponding domains (non-empty sets)

- in this case, $\mathcal{X}$ and $dom$ form a [[plfd]], so $S$ is simply made up of the values of variables within $\mathcal{X}$


- <span id="important">state transition graphs</span> can be used to **visually** represent state transition systems
	- a node is a state
	- there are arcs between nodes for every element in the transition relation $T$

- state transition graphs have a core issue - the number of nodes in the graph is exponential with the number of states and the domain size for the given variables 
- there is a solution for this; symbolic representation

- <span id="important">symbolic representation of sets of states</span>
- propositional formulas can be used to represent specific states, as they all have variables assigned to corresponding values
- as each variable doubles the number of possible states (if the domain for all variables is {0,1}), then we can say that a variable $x$ represents half the states, and $\neg x$ the other half

- <span id="important">symbolic representation of transition relations</span>
- a transition is deterministic if there is at most one state you can travel to from every state
- the same approach in which formulas = states can be applied to transitions, but the main issue is that plfd formulas only express a single state (we need to express 2 states, before/after)
- the workaround for this is duplicating the current state variables to make **next state variables**
- formula $F$ of variables $\mathcal{X} \cup \mathcal{X'}$ represents a transition if $t = \{(s,s')|(s,s')\models F\}$ 

- formulas alone can run into [[planning - the frame problem]] (from AI but relevant) - where variables youre not concerned with aren't mentioned in your formulas, which technically allows unintended transitions to take place
- we use $only(x_1,...,x_n)$ to specify which variable values can be changed by a transition
$$\bigwedge\limits_{y\in X \textbackslash \{x_1,...x_n\}} y = y'$$
i.e. all y not in $x_1,...,x_n$ has the same value as their next state variable

