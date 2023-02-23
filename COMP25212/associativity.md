[[COMP25212]]

in $N$ entry [[caches]], we say that $N$ different items can be stored without restriction

if any entry can be stored in any area in the cache, we say that this cache is ==fully associative== - [[fully associative cache]]

full associativity is ==computationally expensive==, as an entire tag table search is required i.e. $N$ comparisons - for this reason, caches are typically only fully associative when theyre much smaller

CAM is used as an ==associative store== used in fully associative caches - a tag address is fed in, then the corresponding address is returned

[[direct mapped cache]] is basically the opposite of fully associatve cache