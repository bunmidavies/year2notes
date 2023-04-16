[[COMP25212]]

### ~ definition
- table walking involves traversing multiple levels of page tables in order to translate a virtual memory address into a physical memory address ([[virtual memory + page tables]])
- each portion of a virtual address is used to index into a table at a specific level, and the process of going level by level to reach the physical address is table walking
- the translation is typically stored within a TLB, and table walking itself is a result of a TLB miss
- a TLB is just a cache within the [[MMU]] which works in parallel with L1 cache access in order to retrieve page translations with their permissions