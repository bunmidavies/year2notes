[[COMP22111]]

**timing closure** is where a combinatorial logic design is modified to meet timing requirements

in order to determine these timing requirements, there are two main processes:
- simulation: can indicate well if a system fails at a particular clock speed - however, it would have to be exhaustive, and can require a **long** simulation time
- [[static timing analysis]] (**STA**): static means independent of the input state. STA finds all combinatorial logic between flip flops, and analyses the delay between all possible paths between flip flops. STA reports the critical paths with setup and hold time violations