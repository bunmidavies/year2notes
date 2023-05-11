[[COMP25212]]

### definition
- directory based protocols overcome the lack of scalability associated with [[snooping protocols]], by using ==distributed hardware== (similar to distributed hardware used in [[out of order execution with tomasulo]])
- the memory system has a directory which stores information of ==what is being shared==
- this stored info is more complex than the info in snooping protocols
- the messages which were previously broadcast to all devices in snooping protocols, are now ==point-to-point== - the bus is replaced with a network on chip ([[on chip interconnects]])
- now, multiple messages can be transmitted in parallel
![](https://i.imgur.com/1wbH1HZ.png)
- since in this example the directory is centralised, it can still become a bottleneck at some point - by distributing this directory, some scalability issues can be solved
![](https://i.imgur.com/QYz7ZLl.png)

### simple cache line protocols
- cache lines can be in one of 3 states (similar to [[MESI protocol]]):
	1. I = invalid
	2. S = shared - coherent with main memory, other copies may exist
	3. M = modified - value changed, no other copies exist
- the directory itself stores info about cache lines, and these cache lines can be in one of 3 states:
	1. NC = not present in any core's cache
	2. S = cache line is not modified, and in at least one core
	3. M = cache line is modified, and in exactly one core
- the directory uses a ==sharing vector== to know which cores have copies of each cache line

### directory coherence example
![|650](https://i.imgur.com/ncgxFwM.png)

