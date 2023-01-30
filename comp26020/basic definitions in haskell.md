[[COMP26020]] - [[haskell]]

everything we write in haskell is of a particular value, and we can not change it after

`/=` means ==not equals== in haskell

when continuing a definition across a newline, whitespace is needed to indicate. Any new definitions must begin on a newline

`if then else` can be used in definitions, alongside with other operations, e.g.
`v = 7 * (if b then 5 else 6)` - v would either become 35 or 42

to define a function for all values, provide the parameter after the function name
`add7 n = n + 7`

a function can also be defined for particular values over several lines
```Haskell
small 0 = True
small 1 = True
small n = False
```
the order here is important, as this implies everything > 1 must be `False`
further on, this can be defined with cases - [[higher order functions + alternate definitions]]

functions can also operate on pairs - its best to still think of these as arguments on 1 parameter, which happens to be a pair
`addUp (m,n) = m + n`

functions can also be defined recursively, for instance:
```Haskell
fib 0 = 0
fib 1 = 1
fib n = fib(n-2) + fib(n-1)
```