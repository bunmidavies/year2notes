[[COMP25212]]

### out of order execution
- out of order execution simply means ==the original order in a program isnt preserved==
- an out of order processor will execute instructions as input data becomes available
- when ==conflicting instructions== occur ([[data hazards]], [[structural hazards]], and cache misses), pipeline stalls can technically be avoided by processing instructions which are able to ==immediately run== in the meantime
- out of order execution takes advantage of instruction line parallelism, ultimately increasing the number of instructions executed per cycle

### requirements for out of order processors
- an ==instruction buffer== must exist in order to store all issued instructions
- a ==dynamic scheduler== must exist to send non-conflicting instructions to execute: dynamic scheduling should allow instructions behind stalls to proceed (allowing for parallel execution)
- memory/register accesses must be ==delayed== until older instructions are finished (to comply with application semantics)
![ | 550](https://i.imgur.com/lcWw2K5.png)

### dynamic scheduling
![ | 450](https://i.imgur.com/akbpL7Z.png)
