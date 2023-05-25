[[COMP26020]]

- the LR(1) property is useful in order to construct a more efficient and flexible method of [[bottom-up parsing]], known as LR parsing
- a grammar is LR(1) if, given a rightmost derivation, it is possible to:
	- isolate the handle of each right-sentential form
	- determine the production rule to perform reduction with, by scanning the sentential form from left-to-right, going at most 1 symbol beyond the right-end of the handle

### LR Parsing
- LR parsing involves reading tokens from an input buffer, so the same as a shift-reduce parser
- However, extra state information is added after each symbol in the stack - these states summarise information contained in the stack entry below it

![ | 550](https://i.imgur.com/Qyel9VC.png)

- parsing can then be completed with the following skeleton code, as long as the action and goto tables are known

![](https://i.imgur.com/vhhDyRm.png)

### LR parsing with stack + ACTION/GOTO tables

1. take the current state off the top of the stack (without popping), and the next symbol from the current input sentence  
2. check the ACTION - the action table will have either shift/reduce, followed by the new state to be pushed to the stack - when reducing to a non terminal symbol, the GOTO table will state which new state is pushed onto the stack
3. use the `eof` column when the input is empty (i.e. no more terminal symbols to push to stack)
  
example  
![](https://i.imgur.com/hyAZIhP.png)
