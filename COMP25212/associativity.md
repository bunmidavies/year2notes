[[COMP25212]]

in $N$ entry [[caches]], we say that $N$ different items can be stored without restriction

if any entry can be stored in any area in the cache, we say that this cache is ==fully associative==

full associativity is ==computationally expensive==, as an entire tag table search is required i.e. $N$ comparisons - for this reason, caches are typically only fully associative when theyre much smaller

CAM is used as an ==associative store== used in fully associative caches - a tag address is fed in, then the corresponding address is returned

==direct mapped cache== is basically the opposite of full associativity, and simplifies the implementation of a cache, by providing the notion that any particular item has a predetermined place it might be cached in. This is determined by its ==lower address bits==

by using direct mapping, incoming addresses only need one tag comparison, thus lower power is required. Data can be looked up ==speculatively== and in parallel, rather than waiting for the comparisons to resolve

smaller caches with direct mapping will typically have a lot more collisions than larger caches (collisions go donw as cache size increases)