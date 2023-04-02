[[COMP26020]]

### ~ intro + definition
- although processors operate through cycles, not every instruction may be complete after a singular cycle - this means that the processor may have to wait more than 1 cycle
- for example, a load instruction's result may take $n$ cycles to complete - if these instructions can be gotten out of the way as early as possible, then less delays may be required later on
- the aim of instruction scheduling is to ==reorder== instructions in order to produce code which is both ==correct== and ==minimizes execution time==

### ~ list scheduling with precedence graph
- a precedence graph is also known as a ==data dependence graph== - a node represents an instruction in a program, and two nodes are connected if one instruction relies on the result of the other (thus, must wait until it is complete in order to be issued)
- nodes with no connections whatsoever may be executed in any order
- using this graph, a ==priority function== can be calculated - this values each node by taking the latency of its corresponding instruction, and adding the weight of any ==child== nodes (i.e. any instructions that depend on it)
- this priority function now weighs essentially, the most dependent instruction - the node with the greatest weight may take the longest and be required for the most expensive instructions
- a list scheduling algorithm can be defined using this graph, and priority function
```
cycle = 1, ready = set of available operations, active = {}
while (!ready.isEmpty() OR !active.isEmpty())
{
	if ready isnt empty
		operation = pop the highest value operation from ready
		schedule(operation) = cycle
		active.push(operation)
	cycle++
	for each operation in active
		if(schedule(operation) + delay(operation) <= cycle)
			remove operation from active //operation is complete since cycle >= start time + delay
			for each child of operation
				if all operands of child are available
					ready.push(child)
}
```
- note that this priority function can be varied - for instance instead of the weighting implemented here, nodes could be weighted based on its descendants (i.e. instructions it depends on rather than instructions that depend on it)

### ~ forward list scheduling vs backward list scheduling
- ==forward list scheduling== - goes from start to the end of the program - instructions are scheduled as early as possible
- ==backward list scheduling== - starts from the end of the program, and goes backwards - instructions are scheduled as late as possible
- a typical approach within a compiler may be to try both approaches, and then keep the result with the best performance

### ~ register allocation vs instruction scheduling
- it should be noted that register allocation taking place beforehand, may restrict the possible choices for instruction scheduling - for example, depending on how many registers were put in use by register allocation, certain instructions may have to be scheduled for later
- on the other hand, if instruction scheduling takes place first, then certain orderings of instructions may cause more live ranges, which may result in more registers to be required or more memory access to be required as well