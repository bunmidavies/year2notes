[[COMP22111]]

this shouldnt be used as a source of information to revise, but more as a general list, while trying to find which week mentions a certain topic, or a broad view of which topics need to be studied

==these summaries are made based off the ACCOMPANYING NOTES for each video - some points below may mention extra topics the videos don't mention (and the videos COULD mention points that might not be in the notes)==
***
==week 1== - MU0 / Stump
- **video 1**: designing ISAs, VLSI design flow, instruction specification, von neumann vs harvard architecture, von neumman bottleneck, [[addressing modes]], RISC vs CISC, 
- **video 2**: MU0 ISA, MU0 instruction set, operations and status flags, MU0 interface and memory operation (datapath and control, how to read/write from memory)
- **video 3**: Stump ISA, Stump instruction format, Stump [[addressing modes]] (6 main types), type1/type2/type3 instructions, STCC bit, CSH, when to set carry flag, load store instructions
- **video 4**: <span style="color:grey">lab instruction video</span>
***
==week 2== - Verilog
- **video 1**: what is a verilog module, wire, reg, verilog example implementations
- **video 2:** clock and reset, designing an up/down counter, shift register, shift operation in verilog, 
- **video 3:** verilog tasks, verilog functions, structural verilog, explicit description, implicit description, structural mux implementation, car park system
- **video 4:** verification & testing, simulation, 5 design steps, hierarchical approach to testing, unit tests, integration tests, regression tests, the testbench, combinatorial circuit testing, $finish, types of test data, file handling, testing sequential circuits with a clock, self checking testbenches ("golden data")
***
==week 3== - sequential systems + SM charts
- **video 1**: combinatorial vs sequential, summary of sequential systems, control block controls datapath, finite state machines, Stump's fetch execute memory, [[Moore machines vs Mealy machines]], state transition diagram, synchronous paradigm advantages, arm microprocessor + instructions, splitting a system into data and control elements, FSM functional blocks
- **video 2**: SM charts (or ASM charts, same thing), problems with state transition charts, state box, decision box, conditional output box, SM block, link paths, equivalent SM charts, serial/parallel designs, shared decision boxes
- **video 3**: state transition table vs state transition diagram vs SM chart comparisons, recognising a moore/mealy machine in diagrams, moore vs mealy recap, FSM with no datapath examples
- **video 4**: car park example, designing datapath + FSM, the signals required and diagrams
***
==week 4== - LUMP / designing a processor
- **video 0 (no video):** - [[LUMP]] / [[LumpOverview.pdf]]
- **video 1:** MU0 as an example for designing a processor - MU0 interface (i.e. the signals seen by the outside world), Stump interface, FSM = FSM + control signal decode
- **video 2:** top down design flow, MU0 functional blocks - registers, architectural design - the datapath, MU0 fetch phase, MU0 execute phase, architectural to RTL design, MU0 flag logic (no cc register), data paths for mu0 instructions
- **video 3**: stump functional blocks, stump register bank, stump control block, stump fetch execute memory, path usage diagrams for instruction types, 2s complement revisited
- **video 4:** mu0 control block verilog design, pre-compiler directives, implementing the control, signal usage charts, hints for stump implementation, mu0 signals for corresponding instructions
***
==week 5== - CMOS
- **video 1:** [[voltage, current and resistance]], CMOS being a type of MOSFET using pMOS and nMOS ([[MOS]]), water analogy, basic circuits, the resistor, resistors in series and parallel, [[capacitors]], series and parallel combos of capacitors, time constant to charge capacitors
- **video 2:** nMOS, pMOS, nMOS/pMOS transmission properties, example transmission gate, 2-1 mux
- **video 3:** pull-up/pull-down network, CMOS circuit elements, pull-up network = when a 1 is to be outputted (i.e. conduct the power supply), pull-down network = when a 0 is to be outputted (i.e. conduct the ground), CMOS NAND gate, CMOS AND gate using inverter
- **video 4:** factors affecting transistor properties, input load, output impedance, capacitive load proportional to area, nMOS impedance vs pMOS impedance, why NAND logic is preferred over NOR logic, dynamic power dissipation, $P_D \propto C_L \cdot VDD^2$ , implications of stray capacitance, RC circuit delay due to capacitance, methods to reduce signal delay in transistor, unwanted power dissipation while switching signals, $P_S \propto C_P \cdot VDD^2$ and $P_T = P_D + P_S$
***
==week 6== - reading week
***
==week 7== - 