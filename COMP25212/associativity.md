[[COMP25212]]

### ~ definition
- associativity basically defines which memory addresses can be stored with which tags in a cache
- in $N$ entry [[caches]], we say that $N$ different items can be stored without restriction

### ~ fully associative
- if any entry can be stored in any area in the cache, we say that this cache is ==fully associative== - [[fully associative cache]]
- full associativity is ==computationally expensive==, as an entire tag table search is required i.e. $N$ comparisons - for this reason, caches are typically only fully associative when theyre much smaller
- as you reduce associativity, you are essentially reducing the areas which a cache entry for a certain memory address may reside

### ~ direct-mapped cache
- a [[direct mapped cache]] is basically the opposite of fully associatve cache
- any memory address has a ==predetermined== place it may be cached in, which is determined by the memory address's ==lower address bits==
- this means that incoming memory addresses ==only need one tag comparison==
- for this reason, direct-mapping is ==faster and more power efficient== than fully associative caches - the downside of this is that for larger caches, direct mapped caches will begin to run into more cache conflicts, which may cause more eviction than necessary, and result in a higher cache miss rate