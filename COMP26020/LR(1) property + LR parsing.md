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
