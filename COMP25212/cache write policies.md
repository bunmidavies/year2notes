[[COMP25212]]

### ~ intro
- reading from memory using a cache is relatively straightforward, since if you have a hit, you just retrieve the data, and if you have a miss you just grab the data from memory
- however with writing, cache is a ==copy== of the data - this means writing will change the data, causing data stored in the cache to become ==outdated==
- a cache write policy is just the behaviour of a cache when performing a write operation - 4 main write policies are covered here

### ~ write-through vs write-back
- ==write-through = memory is kept up to date when writing to cache==. This means that main memory is updated with every write operation
- ==write-back = only the cache is updated during a write operation== - a cache line is only written back (copied) to main memory when it is replaced
- note that write-back is also called ==copy-back== - these terms are simply interchangeable 
- modified cache lines which actually need to be written to memory can be marked as 'dirty' - this prevents cache lines which never even got modified, from being uneccessarily written back when evicted
![ | 500](https://i.imgur.com/q9uj5Eo.png)

### ~ allocation vs no allocation
- in the case of a write miss, ==allocation means fetching and caching the line containing the data== - meanwhile, no allocation obviously means the opposite - in the case of a write miss you update the data in memory, but do not cache it
- temporal [[locality]] would suggest that performing write allocation would be convenient, as the temporal part suggests if you access this line once you will probably have to access it again soon
- **allocation/no allocation can't exist for reads because the processor requires the cache to contain the data to fulfill its request**

### ~ write-back tradeoffs
- the main advantage of write-back is that a line can be updated several times in cache, without having to update the memory each and every time. This can result in significant ==power saving==, and write-back is generally faster than write-through
- it (obviously) also doesn't matter that the line in main memory is out of date, because if it is in cache then all requests for that line will be satisfied, and responded with correct data
- note that in the case of power loss, your memory never got to update, so this is a possible risk with write-back
