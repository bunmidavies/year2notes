[[COMP25212]]

==set associative cache is a widely implemented compromise between:==
- [[fully associative cache]], and
- [[direct mapped cache]]

- set associative caches implement a small number of direct mapped caches in ==parallel==
- thus, an $n$-way set associative cache ($n$ may be typically 2 or 4) uses $n$ direct mapped caches, and data can be placed in the relevant line of any of these direct ampped caches

### searching set associative cache
- searching a set associative cache involves checking the relevant line (i.e. where the address would map to) across all the direct mapped caches, therefore some kind of associative search on the tag fields takes place