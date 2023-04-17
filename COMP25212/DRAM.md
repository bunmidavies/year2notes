[[COMP25212]]

### ~ definition
- DRAM = Dynamic RAM 
- the memory forgets its contents unless its ==refreshed== at frequent intervals - this is due to DRAM making use of capacitors internally, which leak charge away over time
- theres a limited amount of time in which any cell is valid
- DRAM's 'random access' ability is only approximated to be in constant time - access patterns can noticeably affect timing
- DRAM is ==very compact== - it has the most bits/area of 'RAM', and has moderate power needs

### ~ applications
- DRAM is typically considered to be used in the ==main memory== of workstations, graphics systems, etc.
![ | 400](https://i.imgur.com/9FanHBx.png)


### ~ implementation
- DRAM is implemented on silicon as a 2D matrix (2d array) - a row is picked through a row address, and a column is picked through the column address
- the entire row must be read from, and reading in this matrix is a destructive operation
![](https://i.imgur.com/TWFpLvA.png)
- once the original row has been read, it needs to be restored using the row latch (for reasons mentioned above), which stored the value being read
- internally, data is always handled a whole row at a time - there is a separate row address and column address for every cell
- a modern DRAM chip will typically contain several of the matrices shown above - aka ==banks== - the banks in realy would be stored side by side on the 2D silicon surface, but can be visualised in 3D
- the ==latency== to read a column is much lower if an already 'open' column is being used 0 therefore ==burst access== is an easy way to exploit this feature - reading from consecutive addresses (this relies on allocating the address bits appropriately)

### ~ burst access
- after selecting a row, there is a much lower latency for reading if you continue to read from columns within that row
- ==burst access== is where consecutive addresses are read from, and can be useful in applications like fetching an instruction stream