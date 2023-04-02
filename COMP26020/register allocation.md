[[COMP26020]]

### ~ definition
- register allocation follows on from [[instruction selection]] - at this point, we have some code which makes use of an ==unbounded number of registers== (virtual registers)
- since the machine does not have an unbounded number of registers, the task at hand is:
	- produce runnable code for $k$ registers
	- minimise the number of loads and stores (==spill code==) and space used
	- perform these tasks efficiently

### ~ local vs global register allocation
- there are two main types of register allocation:
	- ==local register allocation== - this takes place in a ==single basic block== - a line of code which is completely branch / control statement free, and all the contained lines will definitely run
	- ==global register allocation== - this takes place across ==multiple basic blocks==
- only simplified cases of local allocation can be solved in linear time - the rest of these problems are NP-complete (i.e. difficult problems)

### ~ liveness / live ranges
- a value of a variable is ==live== between its definition and its uses
- therefore, ==live range = interval between a variables definition, and last use==
- thus, it makes sense that in order for load/stores to never be used, ==live values <= no of registers== would have to be true at all times
- if at a given point there are more live ranges than registers, ==spilling (saving values to memory)== must occur

### ~ top-down register allocation
- in top-down register allocation, registers are reserved for the ==most frequently used values== - any other values are loaded/stored when needed
- this can improve performance, but simultaneously may wrongly prioritise variables used heavily in particular parts of the code, but not at all in a later part (i.e. due to loops etc.)

### ~ bottom-up register allocation
- in bottom-up register allocation, a new register is assigned at the ==start of any live range== (i.e. when any variable is initialised), and that register is returned once the end of the live range is reached
- if a new register needs to be assigned but there are none available, the register which is used the furthest in the future is stored, and this register can now be used

### ~ register allocation via graph colouring
- one method of abstracting the register allocation problem (as part of the part 3 lab) is by building an ==interference graph==, where each node represents a live range, and connected nodes represent overlapping live ranges
- if it is possible to produce a ==k-colouring== of the graph, then no spilling is required - if not, then a larger k is required, which implies spilling must be required
- this k-colouring once successful could then be mapped to physical registers
![ | 600](https://i.imgur.com/a4FbREe.png)

