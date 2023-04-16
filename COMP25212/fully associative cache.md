[[COMP25212]]

- in a fully associative cache, a memory address is searched for throughout the entire tag store
- this is expensive, and a special [[CAM (associative memory)]] block is used for this as shown below
- if the corresponding memory address is found, it can be read from the data RAM
![ | 350](https://i.imgur.com/OVfYfYp.png)

### addressing style
- in the fully associative model for a cache, the ==tag field== is a full byte address, truncated to a multiple of a power of 2 depending on cache line size (remember that a line's data  can be made up of multiple words of data - [[cache lines]])
- for instance:
	- line size of 4 bytes = discard bottom 2 bits
	- line size of 8 bytes = discard bottom 3 bits

### reading data
- to find whether an item is in this cache, the presented address (suitably truncated) is compared with the tag field of each valid line
- comparing every valid line with a presented address typically sounds like it would be slow, but all checks are done in parallel using an associative memory known as [[CAM (associative memory)]]
- ==hit== - after this check is done, as with any cache if the required address was found, then this was a 'hit', and the required value can just be read from the cache line's data field
- ==miss== - if the required address wasnt found, then the data is read from main memory - enough data to fill the complete cache line's data field is copied in (in the attempt of anticipating possible future accesses), and the valid field is updated ([[cache lines]])
- as mentioned, any data can occupy any line, therefore a line must be chosen for this new data (given a hit occured)

### writing data
- ==there are several strategies for writing data to cache/memory==
- writing is more complicated than reading - the first step is to establish if the address to be written to is already in cache
- regardless of whether the address is or isn't in cache, the data will be written to cache
- in the 'write through no allocate' strategy, in both cases this data will be written to main memory so that it is up to date once the write takes place
