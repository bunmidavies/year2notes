[[COMP25212]]

- bandwidth can be increased by wider buses
- latency is a trickier problem to solve, 

A ==write buffer== is a FIFO queue which allows write operations to 'fire-and-forget', improving their latency, since the processor can proceed in parallel

Read operations in a write buffer can overtake queued writes (writes have little latency, while reads have latency)

Write buffers work well for most memory, i.e. RAM, but isn't as good for any things like memory mapped IO etc.