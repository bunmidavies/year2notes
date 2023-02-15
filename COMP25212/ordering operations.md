[[COMP25212]]

there are different ways to order the operations in a [[write buffer]]

### disallowing buffering
- pages may be marked in a page table, or the address may be recognised by hardware
- writes should be completed before the processor can continue - i.e. nothing can be done in parallel

### memory barrier (fence)
- an uncrossable point in the stream of bus requests - all preceding operations must complete before any succeeding operations start (relative to the barrier)

### <span style="color:cyan">victim cache</span>
- a tail and a head is implented in the write buffer, and values keep getting 'forwarded' even after you write them