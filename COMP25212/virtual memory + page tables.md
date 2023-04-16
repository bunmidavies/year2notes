[[COMP25212]]

### ~ definition
- virtual memory is the notion of each process having it's own private address space, which get translated into real physical addresses in memory
- the translations are defined within ==page tables== - these translations can be simplified by assuming locality, i.e. some set of virtual address -> some set of physical addresses, rather than maybe storing translations word by word

### ~ page tables + multi-level page tables
- as mentioned above, page tables store the translations from virtual->physical
- these can get rather large, and multi-level page tables are typically used in place of flat level page tables which would be impractical in terms of size
- one of the main downsides of a multilevel page table is the increased number of lookups, increasing latency in general
![|450](https://i.imgur.com/awMWoQf.png)


### ~ links
- [wikipedia](https://en.wikipedia.org/wiki/Virtual_memory)