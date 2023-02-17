[[COMP25212]]

a [[TLB]] is able to deliver:
- a page translation
- a pages permissions (metadata - definitely needed)

in the case that a TLB misses, it will:
- stall the processor
- perform the page table reads
- cache the new translation
- instigate the L1 cache data fetch
all of this is done in hardware, this is called ==table walking==