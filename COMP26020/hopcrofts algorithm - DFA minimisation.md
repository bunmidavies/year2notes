[[COMP26020]]

- the question at hand given any DFA, is whether the number of states can be minimised
- the answer is yes, **if** we can find ==groups of states== where for each input symbol, every state of this group transitions to another group, or that <u>same group</u>
- the algorithm to minimise a DFA is known as ==hopcrofts algorithm==

### example
- note that the DFA being minimised is from the [[NFA to DFA]] example
- the starting groups are split by ==final== and ==non-final== states
![ | 550](https://i.imgur.com/zFkaf08.png)
- for each ==non singular-member group==, apply all the possible transitions - that is, take each symbol from the language and see where each symbol in the group ends up
- if there is any symbol which goes either:
	- outside the group
	- to a different group from all other symbols in the group
- that symbol will get moved to its own group
- in the last row of the table we see that the groups {E}, {D}, {B}, {A,C} no matter what the symbol, either stay in those groups, or all go to the same group, so that is the final answer

### example 2, NFA -> DFA -> minimised DFA
![ | 550](https://i.imgur.com/MBPl3b8.png)
![ | 550](https://i.imgur.com/QCFoXbE.png)
- in this example, algorithms have managed to produce the same minimised DFA that a human could come up with, as shown in [[thompsons construction - RE to NFA]]