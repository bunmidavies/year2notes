[[COMP25212]]

- in this example, note that we have cache ==lines==, hence the mux underneath the data RAM, the coloured example below doesn't have this
![ | 350](https://i.imgur.com/z9PlkVx.png)
![ | 350](https://i.imgur.com/L2rUUDe.png)


### direct mapped vs full associativity
- ==direct mapped cache== is basically the opposite of full associativity, and simplifies the implementation of a cache, by providing the notion that any particular item has a predetermined place it might be cached in. this is determined by its ==lower address bits==
- note that the bottom bits are usually used because its likely that top bits in memory addresses are similar to each other if not the same

### tag and index
- as with fully associative cache, the address is truncated depending on cache line size
- the truncated address is divided into 2 parts:
	- ==tag== - stored along with the data to be stored
	- ==index== - used to address a cache line directly. The size of the index depends on the number of lines in the cache (i.e. 7 cache lines means 3 bit index to select the line, then the rest is the tag)
- when a new address is presented to the cache, the index is formed and used to address the cache line - the tag of this cache line is then compared to the tag formed from the presented address (this is like ==hashing==) - if they're the same then this is the data that is needed
- if above doesn't apply (i.e. the tags dont match) this is a miss, and similar writing strategies to fully associative caches exist for direct mapped cache

### pros and cons
- direct mapping is really just a hash table implemented in hardware - it is cheaper to implement than [[fully associative cache]] - however, there is an increased chance in having a lower hit rate, due to its inflexible replacement strategy
- smaller caches with direct mapping will typically have a lot more collisions than larger caches (collisions go down as cache size increases)
- you're quite limited as to where a number of memory addresses may be stored in a small direct mapped cache
![](https://i.imgur.com/dtIrkhF.png)

### speculative reading
- since there is only one location a memory address can lie within a cache, this can often allow for a processor to essentially ==gamble==, and fetch data from the corresponding cache tag
- this can be done in parallel, since no comparisons like in a [[fully associative cache]] need to take place, making direct mapped caches ==faster==