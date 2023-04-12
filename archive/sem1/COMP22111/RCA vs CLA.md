[[COMP22111]]

the deep down implementations of the Ripple Carry Adder (**RCA**) and Carry Lookahead Adder (**CLA**) aren't required for COMP22111, but the tradeoffs between the two should be known

RCAs are simple and low cost as they don't require huge circuits. However, the critical path for a RCA is long, and must wait for the previous carry to be calculate, making the RCA relatively slow

with a CLA, you can sensibly evaluate the carry for 3 or 4 bits ahead, which can make the CLA more than 10x faster than the RCA for larger number of bits 

spintronics-based adders also exist (note for this later on ?)