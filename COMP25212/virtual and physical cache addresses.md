[[COMP25212]]

cache entires can be tagged by an address, but there are certain advantages / disadvantages to having either

### virtually addressed cache
- fast: doesn't have to wait for address translation
- however it gets invalidated on context switch
- typically used for L1 cache

### physically addressed cache
- longer access latency
- but may persist over context switches
- typically used for everything below L1