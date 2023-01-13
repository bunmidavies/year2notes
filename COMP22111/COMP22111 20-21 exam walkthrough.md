***
==Question 1==

![[Pasted image 20230110114421.png]]

- ALU and memory operations need to be performed separately, because the calculated address has to be stored in the address register, meaning another state is required ([[STUMP datapath + instruction types + paths]])
- if we were to do both at once the clock frequency and speed of operation would have to be lowered in order to allow for both operations to be done within the same phase
- there can be issues with accessing multiple registers at the same time, so some modification of the register bank / datapath may be required#

***

==Question 2== 

![[Pasted image 20230110114415.png]]

- `shift_op` defined as 3 bits rather than 2 bits in the header
- missing end bracket in instantiation of the shifter
- missing begin and end around test data
- test data is incomplete - no test of `c_in = 1`, doesn't provide confidence in `shift_out` or `c_out` working
- missing test for `2'b00`
- there is no delay between `shift_op = 2'b11` and `$finish`, so nothing wil be observed

***

==Question 3==

![[Pasted image 20230110115136.png]]

1. integration testing
2. regression testing

***

==Question 4==

![[Pasted image 20230110115848.png]]

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

![[Pasted image 20230110120529.png]]

- parallelism is exploited in order for throughput, not for latency

***

==question 6==

![[Pasted image 20230110121203.png]]

- be sure to mention that pipelining ==increases throughput==

***

==question 7==

![[Pasted image 20230110123045.png]]

[[CPU vs GPU vs FPGA]]

==CPU = low latency, low throughput
GPU = high latency, high throughput

***

==question 8==

![[Pasted image 20230110124228.png]]

- chip placement is about placing the netlist onto a chip canvas, in order to optimize power, performance and area


***

==question 9==

![[Pasted image 20230110125838.png]]

- deep reinforcement learning requires no/fewer human experts
- deep reinforcement learning is able to improve from its past mistakes

***

==question 10==

![[Pasted image 20230110130008.png]]

1. `C0`
2. accessed twice, in `LD R4, [PC,#-0x6]` and `LD R5, [PC,#-11]`
3. 0002
4. `LD R4,[R0,#0xB]` and `ST R3,[R0,#0xC]`
5. R4 = 0002, CC = 0001 (c flag gets updated)
6. no, C+Z=1 so condition is not satisfied

***

==question 11==

![[Pasted image 20230110133832.png]]

![[Pasted image 20230110133843.png]]

***

==question 12==

***

==question 13==

***

==question 14==