
[[COMP22111]]
# Week 3
- We focus on designing sequential systems with a control element and datapath element, and how such a design is partitioned

### Combinatorial vs Sequential recap
- Think of a combinatorial circuit as a doorbell - when you press the button, the bell rings. Whenever you press the button, provided its the same doorbell you always get the same ring, so when you press it and whether you've pressed it before isn't relevant to the doorbell

- A sequential circuit could be something like a garage door, where its history / current state is important for how it operates e.g. if the door is already closed, or fully open, this needs to be remembered by the circuit, so some memory is needed
- In almost all sequential circuits, actions are sequenced to an internal clock, and the state is stored within some register. States must be unique values
- **Note that not all sequential circuits need a datapath**. You only need a datapath if there is data to manipulate! The only required thing is that a sequential system has a **Finite State Machine** to control its behaviour
![](https://i.imgur.com/Fsqz5z1.png)

  - This is the Register Transfer Level (RTL) design of the datapath within a sequential circuit. Registers hold data which can then be processed by combinatorial logic to move to another register - on positive clock edges the data moves from one register to logic block, and vice versa

### Sequencing instructions within sequential circuits
- Activities within a typical sequential system need to be sequenced in order to operate
- Stump has 3 stages within each cycle: Fetch, Execute, Memory
- The basic layout for a sequential circuit in terms of what it does is - input data feeds into some 'next state logic' - on the rising edge of a clock, this next state is stored into a register, and becomes the **current state**. Finally, there is some output logic to determine outputs based off the current state, and take according action
- Typically, it's not easy to design a datapath, as well as a control block to work with it

[[SM charts]]

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
![](https://i.imgur.com/JGuz4Uw.png)

+ RTL view as mentioned earlier
![](https://i.imgur.com/cctjXEa.png)


- FSM design:
	- We need 5 states:
	  1. Ready: check if a car is coming in or out
	  2. Inc_tot: increase total if a car is coming in (signals: add, clock enable)
	  3. Cmp: compare count to max (signals: sel = 1, sub (add = 0))
	  4. Closed: if zero from count - max is detected (out signal: disable)
	  5. Dec_tot: decrement (clock enable, (add = 0 for sub))
![](https://i.imgur.com/ZLucXT0.png)
