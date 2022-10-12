# Week 3
- We focus on designing sequential systems with a control element and datapath element, and how such a design is partitioned

### Combinatorial vs Sequential recap
- Think of a combinatorial circuit as a doorbell - when you press the button, the bell rings. Whenever you press the button, provided its the same doorbell you always get the same ring, so when you press it and whether you've pressed it before isn't relevant to the doorbell

- A sequential circuit could be something like a garage door, where its history / current state is important for how it operates e.g. if the door is already closed, or fully open, this needs to be remembered by the circuit, so some memory is needed
- In almost all sequential circuits, actions are sequenced to an internal clock, and the state is stored within some register. States must be unique values
- **Note that not all sequential circuits need a datapath**. You only need a datapath if there is data to manipulate! The only required thing is that a sequential system has a **Finite State Machine** to control its behaviour
  ![[Pasted image 20221010101531.png]]
  - This is the Register Transfer Level (RTL) design of the datapath within a sequential circuit. Registers hold data which can then be processed by combinatorial logic to move to another register - on positive clock edges the data moves from one register to logic block, and vice versa

### Sequencing instructions within sequential circuits
- Activities within a typical sequential system need to be sequenced in order to operate
- Stump has 3 stages within each cycle: Fetch, Execute, Memory
- The basic layout for a sequential circuit in terms of what it does is - input data feeds into some 'next state logic' - on the rising edge of a clock, this next state is stored into a register, and becomes the **current state**. Finally, there is some output logic to determine outputs based off the current state, and take according action
- Typically, it's not easy to design a datapath, as well as a control block to work with it

### Moore Machine vs Mealy Machine
- A moore machine is a sequential system which determines its outputs **only using the current state** - the input changing here doesn't affect the outputs if the state remains the same
- The difference between this and the **Mealy Machine** is that the inputs are connected to the output logic of the system, such that the outputs are determined using **both the current state and current inputs**
- The advantage of the mealy machines is that you may be able to use less states within the system, but issues like timing can arise (due to the asynchronous behaviour)

### SM Charts
- The first step in designing a sequential system is to produce a state transition diagram (circles for states and conditional transitions between circles)
- The problem with these is that they become easily cluttered due to a lot of states
- State Machine (SM) charts can be used instead, and work like flowcharts
- SM Charts have 3 components:
	- State box - A state box has a name, output list, state code, and one output path. It represents one of the finite states the system can exist within
	- Decision box - Looks like a diamond. The box has 2 output paths, true or false, depending on the boolean condition / expression within the box
	- Conditional output box - Entry path is always from a decision box, and has a single exit path. Certain outputs to be assigned are described within the box as a list (**Only available in mealy machines**)
- The SM chart is subdivided into SM blocks, which encapsulates the complete behaviour for a certain state. There can be multiple outputs from the SM blocks, but they must all be unique, and all possible conditions within the SM block must be covered
- Note that all components within an SM block **are evaluated simultaneously**. Contrary to how it may look (arrows implying data may flow from one block to another), everything that is determined within the sm block is done at the same time
- SM charts can be designed in multiple ways but actually give the same behaviour when implemented in hardware (thus being equivalent)
- **Link path extraction** - checking all the valid paths through the SM block are valid, and all boolean conditions are covered by the SM block
- Due to everything being processed in an SM block simultaneously, it also possible that you can design SM blocks in parallel or serially, and they will be equivalent

### Sequential systems w/ no datapath
- A sequential system can have two elements: FSM and datapath. **Only the FSM is a key component of the sequential system**
- We can design a system with an SM chart with no datapath, by assigning the state within state blocks after passing a number of conditions
- Mealy = **Output assignment considers inputs and state**
- Moore = **Output assignment ONLY considers state**

### Producing the RTL design of a datapath
- Example: we are designing an entry/exit car parking system
- Cars are allowed in / out 1 by 1, and the system must show if the carpark is full (+ uses sensors + shows a light to indicate capacity)
- The FSM always carries out expected behaviour
- The RTL datapath performs any data manipulation required by the design

- Behavioural requirements:
	- The total cars is incremented when a car enters, and decrements when the car decrements
	- A sign illuminates to say the carpark is full, and blocks the barrier
	- Our main data is the number of cars in the carpark

- Datapath design:
	- We need a register storing the count of cars in the carpark. It needs a clock enable, and a clock signal
	- We have a basic ALU which has add/sub operations for dealing with carpark count
	- We use a multiplexer to decide whether we're trying to decrement the register count, or compare it to the max size (in order to check if we've reached the limit)
	- If register - max == 0, then a small circuit sends a 'full' signal
- Datapath from video
![[Pasted image 20221010112038.png]]
+ RTL view as mentioned earlier
![[Pasted image 20221010112053.png]]

- FSM design:
	- We need 5 states:
	  1. Ready: check if a car is coming in or out
	  2. Inc_tot: increase total if a car is coming in (signals: add, clock enable)
	  3. Cmp: compare count to max (signals: sel = 1, sub (add = 0))
	  4. Closed: if zero from count - max is detected (out signal: disable)
	  5. Dec_tot: decrement (clock enable, (add = 0 for sub))![[Pasted image 20221010112554.png]]