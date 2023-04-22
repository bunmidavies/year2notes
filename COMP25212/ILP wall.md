[[COMP25212]]

### ~ definition
- the ILP wall = the ==instruction level parallelism wall== 
- essentially, the parallelism possible between ==independent== instructions in 1 thread (i.e. instructions that don't depend on other instructions in that same thread) is limited in many applications
- hardware also imposes limitations, including:
	- no of instructions that can be fetched per cycle
	- instruction window size
- all mechanisms which work to improve single core processors are affected by this notion