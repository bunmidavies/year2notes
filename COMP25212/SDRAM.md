[[COMP25212]]

- SDRAM is the ==modern way to interface DRAM== - it is a form of DRAM which uses a clocked wrapper in order to making timing/interfacing easier
- hence the S in SDRAM standing for ==synchronous== - SDRAM provides high bandwidth burst access, but can still have long latency and scheduling issues, making it typically ==complicated to work with==
- like DRAM, SDRAM can also have multiple banks - which mainly operate independently. A device will typically have (maybe) 8 banks
- low order address bits can be used for the bank in order for the banks to interleave

- every row in every bank must be activated then precharged every few milliseconds, in order to 'refresh' these rows periodically ([[DRAM]])

### line closure
- after reading an SDRAM burst, a row can be left open or closed - the line is left open in the hope that the next request is to the same row, where the read will then be considerably faster
- 