[[COMP25212]]

- the principle of a cache is to ==speed up a spatially small subset of accesses==

within a cache there are two main possibilities when trying to access something: a hit or a miss:
$$T_{ave} = T_{hit} + P_{miss} \times T_{miss}$$
typically, $T_{hit}$ is expressed as 1 because the difference between 90% and 100% is minimal (?)

A cache can be subdivided into two main components:
- ==data field== - hods a copy of a subset of the larger storage space
- ==tag== - a list of addresses which are currently stored

there are 4 main steps when operating a cache:
1. address is checked in tags
2. if address is recognised - hit - send data to output
3. otherwise - miss - address is sent onto memory
4. read memory and output if needed

- SRAM is good for random access and generally fuss-free
- SDRAM is good for big memories with burst access (but less fuss-free)

Caches exploit [[locality]] in order to be useful
Caches can be described with different types of [[associativity]]

there are 3 main types of cache misses:
- ==compulsory== misses: data was not previously used
- ==capacity== misses: cache is full so more space would bex needed
- ==conflict== misses: cache architecture limits tag flexibility (?)