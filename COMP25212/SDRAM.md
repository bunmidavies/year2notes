[[COMP25212]]

### ~ definition
- SDRAM is the ==modern way to interface DRAM==
- SDRAM uses the system clock in order to operate synchronously
- hence the S in SDRAM standing for ==synchronous== - SDRAM provides high bandwidth burst access
- SDRAM can still have long latency and scheduling issues, making it typically ==complicated to work with==
- like DRAM, SDRAM can also have multiple banks - which mainly operate independently. A device will typically have (maybe) 8 banks
- low order address bits can be used for the bank in order for the banks to interleave
- every row in every bank must be activated then precharged every few milliseconds, in order to 'refresh' these rows periodically ([[DRAM]])

### ~ line closure
- after reading an SDRAM burst, a row can be left open or closed
- by leaving the row open, you reduce latency for the next access (provided it is on the same row)
- by closing the row, you reduce latency for the next access if a different row is needed
- in short, by gambling and leaving the row open you have a much lower latency if the guess was correct, but a higher latency than normal otherwise

### ~ SDRAM controllers
- an SDRAM controller translates processor / bus operations into appropriate command sequences for the SDRAM chips
- SDRAM controllers can schedule and interleave requests coming from multiple sources, with the correct timing at a high efficiency
![](https://i.imgur.com/fkMotJt.png)

### ~ addressing
- unlike with 'true' RAM, its relevant as to which address bit is used where in a memory address
- the positioning is important since the timing of the address bits can determine when the SDRAM module starts to read / write data
![ | 450](https://i.imgur.com/DODvwVt.png)
