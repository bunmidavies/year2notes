[[COMP25212]]

- a scoreboard is a data structure, implemented as a ==centralized hardware mechanism==,- they exist within [[out of order processors]] to keep track of the different instructions being executed at any given time, and manage [[data dependencies]] between instructions to prevent [[data hazards]]
- in real life scoreboards can be found in processors made by intel, AMD and ARM

### information within the scoreboard
- ==instruction status== - the stage which an instruction is currently in is stored by the scoreboard
- ==functional unit status== - the state of all functional units are stored by the scoreboard - there are 9 main fields for each FU:
![](https://i.imgur.com/Ry1Fl1q.png)


- ==register result status== - the current functional unit which a register lies within

![ | 450](https://i.imgur.com/kERKgzW.png)

### scoreboard pipeline stages
- note that the scoreboard always issues instructions in the given ==program order==, but all other stages can be done ==out of program order==

1. ==issue (ID) ==- an instruction is decoded, and structural / WAW hazards are checked for ([[data dependencies]]) - if a suitable functional unit is free (no structural hazards) and any other active instructions dont have the same destination register (no WAW), then the scoreboard issues the instruction to that free functional unit, and updates any info. If either a structural hazard/WAW exists, the instruction issue must be stalled and no further instructions are issued until the hazards are cleared
2. ==read operands (RO)== - wait until there are no data hazards, then read operands required for execution. A source operand is available if no earlier issued instruction is both active, and going to write to it (no RAW dependency). Once all the source operands are available, the scoreboard tells the functional unit to proceed to exection
3. ==execution (EX)== - the functional unit which holds an instruction and its operands will now execute the actual instruction, and notify the scoreboard when the result is ready
4. ==write result (WB)== - the instruction has a result, and execution has been finished within the functional unit, therefore the scoreboard checks for WAR hazards, and if there are none the results can be written. If there is a WAR hazard, then this stage is stalled

### scoreboard limitations
- the amount of parallelism available within the scoreboard is the amount of parallelism among the instruction - basically out of order execution can't benefit from parallelism if an application doesn't have any parallelism
- centralised structures arent very scalable - the structures scale more than linearly with:
	- no. of score entries (size of the window of instructions)
	- no. of types and functional units