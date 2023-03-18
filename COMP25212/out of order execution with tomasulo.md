[[COMP25212]]

- in Tomasulo's, control logic for out of order execution is decentralised
- there are ==reservation stations== in the functional units which keep instruction info - these also perform ==register renaming== in hardware (in order to avoid WAW and WAW [[data dependencies]])
- the reservation stations also track operands and buffer them as soon as they are available
- there is a [[common data bus]] which is used for functional units to broadcast their results

- there are 3 main stages in the tomasulo algorithm:
	1. Issue - get instruction from FP Op queue (?)
	2. Execute - operate on operands
	3. Write result - finish execution

- advantages of tomasulo
	- distributed hazard detection logic
	- avoids stalling due to WAW/WAR hazards

- drawbacks of tomasulo
	- increased complexity within hardware
	- performance is limited by the [[common data bus]]