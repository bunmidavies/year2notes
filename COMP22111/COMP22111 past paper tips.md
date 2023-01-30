- If a question asks about a data going into a multiplexer, ==be sure to talk about both inputs of the multiplexer==. It is not enough to just talk about the input that is mentioned

- LUTs are good for emulation, ==but do not scale well==

- Be sure to mention ==which phase== the processor is in when asked about what certain components do. For instance, if asked about what the `add1` component does, be sure to mention it increments the PC ==during the fetch phases==

- *An ISA is the interface between software and hardware, and is the ==standardised description== of how a processor works at the most basic level, providing instructions to run software on it. Common examples include ARM and x86

- The PC is ==ALWAYS== incremented in the fetch phase

- in a load/store architecture, operations are only performed to ==data held in local registers== (data is ==not held in memory==). This means:
	- operands come from a local register
	- operation results are written to a register

- there are 3 main types of pipeline hazard:
	- ==data==: data required exists in a different instruction on a different pipeline
	- ==hardware==: two pipelines attempt to access the same hardware at the same time
	- ==control==: a branch is to be followed but instructions ahead of this branch have been fetched

- floating point units are ==required== to represent very large and very small numbers in an ==economic manner==

- reasons for ==not using an FPU==:
	- application doesnt need an FPU
	- application is supposed to be ==low power consuming==
	- FPU is ==too expensive== for the application**

- with bfloat16 - a smaller float size means ==faster calculation== as well as ==less storage== (applicable for ML)

- mu0 has ==8 instructions==