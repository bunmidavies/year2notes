[[COMP25212]]

### ~ factors
cache architecture is a compromise, there are a number of factors to consider:
- ==Size==: available space
- ==Expected use== - localilty = cach line size
- ==Associativity== - high associativity in smaller caches provides noticeable advantages, while low associativity is still simpler, faster and lower power ( the main disadvantage of lower associativity is that there are more misses which contribute to slowness and power draw )
- ==Power== - higher associativity = more activity

- a general PC may use multiple levels, which are suited to different situations, and differ in terms of the characteristics above - e.g. L1, L2, L3, ...
![ | 550](https://i.imgur.com/hMJvswu.png)

