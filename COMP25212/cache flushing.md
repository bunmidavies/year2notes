[[COMP25212]]

### ~ definition
- a cache flush is required when something critical changes - an example of this is a ==context switch== within the processor
- since processes typically deal with virtual addresses, the current cache becomes invalid since the address map changes
- in write-back/copy-back [[cache write policies]], all the cache lines marked 'dirty' must be written back to main memory before the switch - this is known as ==flushing==
- due to the memory writes, this is typically an expensive operation