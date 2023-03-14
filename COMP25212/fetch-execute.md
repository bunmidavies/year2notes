[[COMP25212]]

- already basically covered within COMP15111 last year, fetch-execution is just a simple cycle which repeats within processors
![ | 250](https://i.imgur.com/MYjp7LV.png)
- the fetch and execute parts can be further subdivided:
- ==fetch==:
	- get instruction from memory
	- decode instruction and select registers
- ==execute==:
	- perform the operation / calculate address
	- access an operand in data memory
	- write the result to a register

- by subdividing the fetching and execution, we've designed a ==worst case data path==, which is able to work for all instructions (even if some instructions may not need for instance an operand from memory, or to writeback anything)

![](https://i.imgur.com/68o6fY5.png)
