[[COMP25212]]

### ~ definition
- the memory coherence problem typically affects multicore systems, and is as follows - a core will write to a location in its L1 cache, and other L1 caches may hold shared copies - since the core just updated that location in its cache, the other L1 caches become ==out of date==
- this is essentially the same problem that a singular cache faces with main memory when written to, but extended to multiple cores
- the core has 2 main options:
	1. write through to main memory
	2. copy back only when the cache line is rejected
- this follows the same idea as [[cache write policies]], but ==just updating memory isn't sufficient==, since other cores can hold the same location in its L1 cache