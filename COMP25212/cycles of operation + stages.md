[[COMP25212]]

- most logic circuits are driven by a clock, and in the most simple form of a processor, we assume that ==1 instruction = 1 clock cycle== - this is also known as a ==single-cycle processor==
- this 1 instruction per cycle model makes the assumption that all of the stages in the [[fetch-execute]] cycle take an equal amount of time
- we also assume a perfect cache replacement strategy exists, in order to allow for everything to be done within 1 cycle
![](https://i.imgur.com/Mtwk0fm.png)
- the instruction is broken up into 5 stages - ==IF, ID, EX, MEM, WB==
- ==each block is only being useful for 1/5th of a cycle==
- this leads to the question of can this be done any better, in order to increase utilisation and ultimately ==accelerate execution== - the answer is yes, and is achieved through [[pipelining]]

### why 5 stages?
- early pipelined processors determined that dividing a cycle into 5 stages of roughly equal complexity was appropriate
- pipelined processors today have used 30+ stages, but 5 is only considered here for simplicity