[[COMP25212]]

- Cache is a ==copy== of the data - this means writing will change the data, causing data stored in the cache to become ==outdated==

- There are two main ways to avoid outdated cache:
	- Write-through cache: modifying the cache entry and memory copy when you write new data
	- Copy back/ Write back: Modify the cache entry only (==making the memory itself outdated==)
	  Faster + low power, but due to the memory becoming out of date, the cached data must be copied back to memory on ==eviction== (and the modified lines are labelled as `dirty`)