[[COMP25212]]

### ~ intro + definition
- bandwidth can be increased by wider buses, but something like latency does not depend on bus width at all
- read operations are only complete once you have the data - this means you technically ==have to wait==, since you can't just say the read operation is complete when you don't have the data to show for it
- meanwhile with a write operation, there is the notion of 'fire-and-forget', since you don't require on returned data with a write operation
- a ==write buffer== is a FIFO queue which allows write operations to 'fire-and-forget', improving their latency, since the processor can proceed in parallel
- instead of waiting for the actual moment the data is written into memory, with the write buffer you can count the write operation as being complete once it's reached the queue, and this ==improves latency==
![ | 450](https://i.imgur.com/vPoAg69.png)
- the idea of read operations being able to overtake queued writes brings in the notion of out of order memory operations, which can have its benefits
- the main risks which are introduced now are things like reading outdated versions of data
- write buffers work okay for most 'memory' i.e. ordinary RAM, but is not as good for memory mapped I/O

### ~ ordering operations
- for various reasons, buffering may be disallowed or certain orders of reads/writes may have to be enforced - below are some typical scenarios
	1. ==disallowing buffering==: common for I/O - typically buffering may be disallowed by making this known through the page table (via a marking), or having hardware recognise disallowed addresses - within the write buffer, any write operation with buffering disallowed would be forced to complete until the processor continues (stalling)
	2. ==memory barriers / fences==: this barrier is an uncrossable point in the write buffer's queue itself - ==all== operations before the fence must complete before suceeding operations start
	3. ==victim cache==: a more advanced topic, but involves storing recently evicted parts of cache which may still be useful (?)

![ | 450](https://i.imgur.com/J9CXFCe.png)
