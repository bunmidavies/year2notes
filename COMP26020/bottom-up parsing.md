[[COMP26020]]

- the goal of bottom-up parsing is to construct a parse tree for a string (sentence), by starting from the leaves of the tree, and working to the root (i.e. from the input sentence back to the starting symbol $S$)

![](https://i.imgur.com/bwKsKB1.png)

- in order to derive a previous derivation from the current derivation, some ==terminal symbol== i.e. $b$ in the current derivation must be found as the right-hand side of a production rule, and replaced with the non-terminal symbol on the left-hand side of the production rule, $A$ - this is called a ==reduction==

### finding reductions + algorithm
- the substring $b$ which matches the right-hand side of that production rule, and occurs as a single step in the righmost derivation is called a ==handle==
- a handle of ==right-sentential form== is a pair $<A\rightarrow b,k>$ where $A\rightarrow b$ is a production rule, and $k$ is the position of $b$'s rightmost symbol
- if a grammar is unambiguous, every sequence of symbols (terminal/non-terminal) which occurs in a rightmost derivation must have a unique handle
- so if these handles are known, then a derivation must exist

thus to construct a rightmost derivation, the following algorithm can be applied
```
for i=n to 1, step - 1:
	find the handle <A->b,k> in current derivation
	replace b with A to generate new derivation //derivation 1 step back
```

one way this can be implemented is using a ==shift-reduce== parser, which uses a ==stack== to hold grammar symbols, and an input buffer to hold the string to be parsed. There are 4 main operations:
1. ==shift== - next input is shifted onto the top of the stack
2. ==reduce== - right end of the handle is on top of the stack - locate left-end of handle in stack, pop handle off stack and push appropriate non-terminal left-hand side symbol
3. ==accept== - parsing ends with success
4. ==error== - call error recovery routine

![ | 550](https://i.imgur.com/Y9zKqsR.png)


### shift-reduce example

![ | 550](https://i.imgur.com/jU5iEnc.png)

### problems with shift-reduce
- there can be times where the parser does not know whether to shift or reduce - this is typically caused due to ambiguous grammars, therefore the common solution is to modify the grammar (or resolve in favour of a shift)
- there can be times where the parser does not know which one of several possible reductions should be made
- the key to efficient bottom-up parsing lies within what handle-finding mechanism is being used

![ | 550](https://i.imgur.com/t9b3Ypo.png)
