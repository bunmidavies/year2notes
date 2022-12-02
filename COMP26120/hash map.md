[[COMP26120]]

## load factor of a hash map
- load factor is simply $\frac{n}{m}$, where:
	- $n$ = no of objects
	- $m$ = hash map capacity
- load factor > 1 means a bucket has more than one entry (not possible with [[open addressing]])
- load factor = 0.5 means the hash map is half full
- <span id="important">as the load factor approaches 0, more and more space is being wasted</span>


## complexity of a hash map
- in the worst case, all keys of a hash map collide, and all operations become linear
- the operations of a hash map are:
	- space
	- insert
	- find
	- remove
- the average case is typically O(1) for all of these operations (except space), but some assumptions are made
- **assumptions**:
	- hash function is uniform
	- load factor < 1
	- operations are in constant time

## rehashing
- rehashing is the process of creating a new table that is a fixed percentage larger of the current table
- all existing elements are reinserted
- rehashing is done when the load factor reaches a particular level (e.g. in open addressing between 0.5 and 0.75)