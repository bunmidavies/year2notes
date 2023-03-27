[[COMP26020]]

- the question at hand given any DFA, is whether the number of states can be minimised
- the answer is yes, **if** we can find ==groups of states== where for each input symbol, every state of this group transitions to another group, or that same group

### example
- note that the DFA being minimised is from the [[NFA to DFA]] example
- the starting groups are split by ==final== and ==non-final== states
![ | 550](https://i.imgur.com/zFkaf08.png)
- as noted in the second bullet point from the start, once we have groups of states on which for each input symbol, every group transitions to another group or stays in its own group, we can now partition these and have the same DFA as before
- in the last row of the table we see that the groups {E}, {D}, {B}, {A,C} no matter what the symbol, either stay in those groups, or all go to the same group, so that is the final answer

### example 2, NFA -> DFA -> minimised DFA
![ | 550](https://i.imgur.com/MBPl3b8.png)
![ | 550](https://i.imgur.com/QCFoXbE.png)
- in this example, algorithms have managed to produce the same minimised DFA that a human could come up with, as shown in [[thompsons construction - RE to NFA]]