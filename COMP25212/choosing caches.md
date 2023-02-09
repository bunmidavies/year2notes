[[COMP25212]]

cache architecture is a compromise, there are a number of factors to consider:
- ==Size==: available space
- ==Expected use== - localilty = cach line size
- ==Associativity== - high associativity in smaller caches provides noticeable advantages, while low associativity is still simpler, faster and lower power ( the main disadvantage of lower associativity is that there are more misses which contribute to slowness and power draw )
- ==Power== - higher associativity = more activity
