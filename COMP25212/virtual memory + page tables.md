[[COMP25212]]

### ~ definition
- virtual memory is the notion of each process having it's own private address space, which get translated into real physical addresses in memory
- the translations are defined within ==page tables== - these translations can be simplified by assuming locality, i.e. some set of virtual address -> some set of physical addresses, rather than maybe storing translations word by word

### ~ page tables + multi-level page tables
- as mentioned above, page tables store the translations from virtual->physical
![|550](https://i.imgur.com/5xkie78.png)
- ==the example above shows addresses in hex==
- pages are usually all of a fixed size - for instance in the example above, pages have a size of 4KB, therefore to address each byte, 12 bits are used ($2^12 = 4096$)
- the page number just selects which page will store the translation from virtual->physical

### multi level page tables
- regular page tables can get rather large, and multi-level page tables are typically used in place of flat level page tables which would be impractical in terms of size
![](https://i.imgur.com/LJLd8QU.png)
- now, the virtual address has 3 parts:
	- high bits (very left 0x000) are still used to index the main page table - but now, the entries within the main page table ==point to another page table==
	- middle bits (0x001) - this finds an entry within the second page table found via the high bits - entries within this table now point to a specific page
	- low bits (0x144) - this is now used as the regular page offset, to retrieve the physical address
- there are two main upsides of this:
	1. if an entire chunk of page table entries are invalid in a second level page table, the main page table entry pointing to these second level entries can just be made invalid, saving a bunch of useless entries - compare this to a flat level page table, where all of these invalid page table entries will just have to sit there
	2. secondary page tables can now be swapped in and out of memory when they're not required, such that more space is saved - these secondary page tables can get swapped in  if needed for a translation
- one of the main downsides of a multilevel page table is the increased number of lookups, increasing latency in general
![|450](https://i.imgur.com/awMWoQf.png)


### ~ links
- [wikipedia](https://en.wikipedia.org/wiki/Virtual_memory)
- [duke - virtual memory + page tables](https://people.duke.edu/~tkb13/courses/ece250-2019su/resources/umass-trekp-csc262-lecture8-virtualmemory.pdf)
- [good video (2 level page table)](https://www.youtube.com/watch?v=Z4kSOv49GNc)
- [ostep chapter on paging](https://pages.cs.wisc.edu/~remzi/OSTEP/vm-smalltables.pdf)