[[COMP26020]]

there are two main steps in top-down parsing:
1. begin with starting symbol of the grammar (parse tree root)
2. repeat until you fully match the input string:
	- find the ==leftmost non-terminal symbol==, $A$
	- select a production rule with $A$ on its left-hand side, and replace it with the right-hand side
	- match any terminal symbols to the input string

the key lies in picking the right production rule, otherwise the parser would need to backtrack - this is generally easy to do as a human, but is more difficult to do as a compiler

### example
for clarity, the left most non-terminal symbol at any given point during the parsing is underlined in light blue
![](https://i.imgur.com/vPtsDJN.png)
in the non-termination example on the right, what is being demonstrated here is a ==left-recursive grammar==

- a left-recursive grammar is simply a grammar which has a non-terminal symbol $A$ such that there is a derivation $A->Aa$ for some string $a$
- they can typically cause top-down parsers to go into an infinite loop
- in order to ==eliminate left-recursion==, its sufficient to replace $A \rightarrow Aa|b$ with $A\rightarrow aA|\varepsilon$ and $A\rightarrow bA$ (the empty symbol still allows the same expression as before)

### lookahead
- for any rule $A \rightarrow B | C$ in a grammar (where A, B and C are all non-terminals), we want a distinct way of choosing the correct production rule to use - this is known as the [[LL(1) property]]
- in order to achieve this, looking ahead in input can be implemented
- most programming languages fall into subclasses of CFGs which can be parsed with very limited lookahead, though an arbitrarily large amount may be needed in general