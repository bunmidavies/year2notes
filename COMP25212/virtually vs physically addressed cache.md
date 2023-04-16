[[COMP25212]]

### ~ intro
- cache entires are tagged by the corresponding memory address being stored
- however, since address spaces can exist both virtually and physically, there is the question of whether caches are tagged using the virtual addresses, or the physical addresses

### virtually addressed cache
- fast: doesn't have to wait for address translation
- however it gets ==invalidated== on context switch - on context switch, there is a new mapping of virtual addresses to physical addresses, so the virtual addresses being stored by a cache may not match up at all
- typically used for L1 cache

### physically addressed cache
- longer access latency, since the address translation from virtual->physical is required
- but may persist over context switches
- typically used for everything below L1

![ | 450](https://i.imgur.com/bzJcRB2.png)
- note how there is a ==TLB== going out to the physical cache, since a translation from virtual->physical address is required