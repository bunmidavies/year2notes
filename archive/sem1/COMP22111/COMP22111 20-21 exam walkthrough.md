***
==Question 1==

![](https://i.imgur.com/GKX5aFB.png)


- ALU and memory operations need to be performed separately, because the calculated address has to be stored in the address register, meaning another state is required ([[STUMP datapath + instruction types + paths]])
- if we were to do both at once the clock frequency and speed of operation would have to be lowered in order to allow for both operations to be done within the same phase
- there can be issues with accessing multiple registers at the same time, so some modification of the register bank / datapath may be required#

***

==Question 2== 

![](https://i.imgur.com/H7I4MgY.png)


- `shift_op` defined as 3 bits rather than 2 bits in the header
- missing end bracket in instantiation of the shifter
- missing begin and end around test data
- test data is incomplete - no test of `c_in = 1`, doesn't provide confidence in `shift_out` or `c_out` working
- missing test for `2'b00`
- there is no delay between `shift_op = 2'b11` and `$finish`, so nothing wil be observed

***

==Question 3==

![](https://i.imgur.com/Xcej5wB.png)


1. integration testing
2. regression testing

***

==Question 4==

![](https://i.imgur.com/2ebPvmf.png)


- as the design is sequential, be sure to use ==non blocking assignment==
- as reset is active low, you are checking for when it turns to 0, hence the ==negedge==

```verilog
always @ (posedge clock, negedge reset, posedge preset)
if(~reset)
	Q <= 0;
else if(preset)
	Q <= 1;
else if(CE)
	Q <= D;
```

***

==question 5==

![](https://i.imgur.com/97qLaPK.png)


- parallelism is exploited in order for throughput, not for latency

***

==question 6==

![](https://i.imgur.com/VnK9OMM.png)


- be sure to mention that pipelining ==increases throughput==

***

==question 7==

![](https://i.imgur.com/jrNEToY.png)


[[CPU vs GPU vs FPGA]]

==CPU = low latency, low throughput
GPU = high latency, high throughput

***

==question 8==

![](https://i.imgur.com/CsqteSm.png)


- chip placement is about placing the netlist onto a chip canvas, in order to optimize power, performance and area


***

==question 9==

![](https://i.imgur.com/YKQZK8u.png)


- deep reinforcement learning requires no/fewer human experts
- deep reinforcement learning is able to improve from its past mistakes

***

==question 10==

![](https://i.imgur.com/obWmcml.png)


1. `C0`
2. accessed twice, in `LD R4, [PC,#-0x6]` and `LD R5, [PC,#-11]`
3. 0002
4. `LD R4,[R0,#0xB]` and `ST R3,[R0,#0xC]`
5. R4 = 0002, CC = 0001 (c flag gets updated)
6. no, C+Z=1 so condition is not satisfied

***

==question 11==

![](https://i.imgur.com/Zj7d7Wk.png)


![](https://i.imgur.com/kHo7Uun.png)


***

==question 12==

***

==question 13==

***

==question 14==