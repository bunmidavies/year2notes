[[COMP25212]]

- DRAM = Dynamic RAM - the memory forgets its contents unless its ==refreshed== at frequent intervals - this is due to DRAM making use of capacitors internally, which leak charge away over time. This means theres  alimited time in which any cell will remain valid
- DRAM's 'random access' ability is only approximated to be in constant time - access patterns can noticeably affect timing
- like [[SRAM]], DRAM is very compact - it has the most bits/area of 'RAM'

- DRAM is implemented on silicon as a 2D matrix (2d array) - a row is picked through a row address, and once their charge is read they're gone
![](https://i.imgur.com/TWFpLvA.png)
- once the original row has been read, it needs to be restored using the row latch (for reasons mentioned above)
- internally, data is always handled a whole row at a time - there is a separate row address and column address for every cell

- a modern DRAM chip will typically contain several of the matrices shown above - aka ==banks== - the banks in realy would be stored side by side on the 2D silicon surface, but can be visualised in 3D
- the ==latency== to read a column is much lower if an already 'open' column is being used 0 therefore ==burst access== is an easy way to exploit this feature - reading from consecutive addresses (this relies on allocating the address bits appropriately)