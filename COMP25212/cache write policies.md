[[COMP25212]]

- A cache write policy is just the behaviour of a cache when performing a write operation
- The content covers 4 main write policies

### write-through vs write-back
- ==write-through = memory is kept up to date when writing to cache==. This means that main memory is updated with every write operation
- ==write-back = only the cache is updated during a write operation== - a cache line is only written back (copied) to main memory when it is replaced
- note that write-back is also called ==copy-back== - these terms are simply interchangeable 

### allocation vs no allocation
- in the case of a write miss, ==allocation means fetching and caching the line containing the data== - meanwhile, no allocation obviously means the opposite - in the case of a write miss you update the data in memory, but do not cache it
- temporal [[locality]] would suggest that performing write allocation would be convenient, as the temporal part suggests if you access this line once you will probably have to access it again soon
- **allocation/no allocation can't exist for reads because the processor requires the cache to contain the data to fulfill its request**

### write-back tradeoffs
- the main advantage of write-back is that a line can be updated several times in cache, without having to update the memory each and every time. This can result in significant ==power saving==
- it (obviously) also doesn't matter that the line in main memory is out of date, because if it is in cache then all requests for that line will be satisfied, and responded with correct data
