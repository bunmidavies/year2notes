[[COMP24011]] / #comp24011 

PageRank is an [[information retrieval]] algorithm, used on sites like ==Google==

The definition of the PageRank of some page $p$ is ==recursive==

$$PR(p) = \frac{1-d}{N} + d\sum_i\frac{PR(in_i)}{C(in_i)}$$

- $N$ = the total number of pages in the collection (==the internet==)
- $in_i$ = ==in-links== to $p$, so $C(in_i)$ = count of out-links on $in_i$
- $d$ = damping factor (probability a web surfer clicks on link)

- in-links = links ==to== a page
- out-links = links ==from== a page