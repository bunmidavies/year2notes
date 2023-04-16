[[COMP25212]]

### ~ principle of caches
- the principle of a cache is to ==speed up a spatially small subset of accesses==
- caches exploit [[locality]] in order to be useful
- caches can be described with different types of [[associativity]]
- within a cache there are two main possibilities when trying to access something: a hit or a miss:
$$T_{ave} = T_{hit} + P_{miss} \times T_{miss}$$
- example:
	- $T_{hit}$ = 1ns (time for access with cache hit)
	- $T_{miss} = 10ns$ (time for access with cache miss)
	- $P_{miss}$ = 10% (probability of accesses resulting in cache miss)
- therefore, 1 + (0.1 * 10) = 2ns average access time

### ~ components of a memory cache
- a cache can typically be subdivided into two main components:
	- ==tags== - a list of addresses which are currently being stored
	- ==data field== - holds the corresponding data being held in the tagged locations

### ~ typical operation of a cache
there are 4 main steps when operating a cache - i.e. accessing a specific memory address:
1. address is checked in tags
2. ==hit==: address is recognised - send data field to output
3. ==miss==: address is sent to memory
4. read memory and output (if a miss occured)
![ | 300](https://i.imgur.com/HR8bT0n.png)

### ~ cache misses
there are 3 main types of cache misses:
- ==compulsory== misses: data was not previously used
- ==capacity== misses: cache is full so more space would be needed
- ==conflict== misses: cache architecture limits tag flexibility - for instance, 2 memory addresses mapping to the same tag in a [[direct mapped cache]]
- for reasons above, ==conflict misses cant occur in fully assoc caches==, and are most frequent in small direct mapped caches