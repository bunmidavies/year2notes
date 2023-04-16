[[COMP25212]]

### ~ definition
==set associative cache is a widely implemented compromise between:==
- [[fully associative cache]], and
- [[direct mapped cache]]
- set associative caches implement a small number of direct mapped caches in ==parallel==
- $n$-way set associative cache = $n$ direct mapped caches, and data can be placed in the mapped line of any of these direct mapped caches
- $n$ may be typically 2,4,8...
- this will reduce the number of ==conflict misses== which could only normally ever occur in direct mapped caches
![ | 350](https://i.imgur.com/1qGrQa6.png)



### ~ searching set associative cache
- searching a set associative cache involves checking the relevant line (i.e. where the address maps to) across ==all the direct mapped caches==
- e.g. searching a 4-way set associative involves searching 4 direct mapped caches