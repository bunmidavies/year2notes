[[COMP26020]]

- converting an NFA to a DFA mainly consists of combining existing states in the NFA to form new states - this is done with ==two fundamental operations==:
	- move($s_i$,$a$) - the union of a set of states to which there is a transition from state $s_i$, using the symbol $a$
	- $\varepsilon$-closure($s_i$): the union of the set of states by using the empty symbol ($\varepsilon$) at state $s_i$ (the state being operated on is always included in the result)
- in relation to [[building scanners]], after converting the NFA to a DFA, the next step is [[hopcrofts algorithm - DFA minimisation]]

### rules
![ | 550 ](https://i.imgur.com/n3z6AHH.png)
- basically, to get the reachable states from any given set of states, you need to figure out which ones you can move to using a symbol, then take the extra states which you can reach by doing nothing (i.e. epsilon) 
- any states including final states from the original NFA, becomes a finite state in the resultant DFA
- the process is complete once it isn't possible to find any new states using the move or epsilon closure operations
- while doing this, it can help to write a ==transition table==, identifying which input symbols result in which states from any other state

### example - $(a | b)*abb$
![ | 550](https://i.imgur.com/2gEHpbm.png)
![ | 550](https://i.imgur.com/pQM3zwj.png)

### example 2 (same RE, different NFA)

![](https://i.imgur.com/fSzxAHL.png)
- the resultant DFA, is the same DFA in the first example

### links
- [regex -> nfa -> mindfa](https://cyberzhg.github.io/toolbox/nfa2dfa)