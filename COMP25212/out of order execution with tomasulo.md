[[COMP25212]]

### definition
- in Tomasulo's, control logic for out of order execution is decentralised
- there are ==reservation stations== in the functional units which keep instruction info - these also perform ==register renaming== in hardware (in order to avoid WAW and WAR dependencies)
- the reservation stations also track operands and buffers them as soon as theyre available:
	- this reduces pressure on the register bank
	- the impact of RAW dependencies is also reduced
- there is a [[common data bus]] which is used for functional units to broadcast their results - this also means that only a single instruction can finish with each cycle
- however, since these reservation stations are distributed and dont know about their neighbours, this allows for a larger window of instructions, and more flexible dynamic scheduling

- there are 3 main stages in the tomasulo algorithm:
	1. Issue - get instruction from FP Op queue, one the reservation station has no structural hazards
	2. Execute - operate on operands once both source operands are ready - if not ready, watch CDB for results
	3. Write result - finish execution, writing to all awaiting units, and freeing the reservation station

- advantages of tomasulo
	- distributed hazard detection logic
	- avoids stalling due to WAW/WAR hazards

- drawbacks of tomasulo
	- increased complexity within hardware
	- performance is limited by the [[common data bus]] - only one instruction can ever be completed per cycle, unless more CDBs are introduced