[[COMP22111]]

==shifter and shift register is used interchangeably, they are the same thing==

a shift register is a cascade of flip flops, meaning the output of each flip flop is connected to the next flip flop. Therefore with each clock transition the lsb within the register is shifted out, and any input can be shifted into the msb

the main types of shifter include:
- one-place shifter: shifts a bit by 1 place in 1 direction per cycle
- bidirectional shifter: shifts a bit in either direction by 1 place per cycle
- barrel shifter: shifts an arbitrary number of places in one operation

the barrel shifter is the ==most expensive circuit== in terms of wiring. One way to implement it is as a sequence of multiplexers, having the output of one multiplexer connected to the input of the next multiplexer

for floating point operations, the mantissas of the two numbers must be aligned, which requires shifting such that the exponents of the two numbers match eachother. This is easy to do with the barrel shifter as you can just shift the smaller number by the difference in the two exponents