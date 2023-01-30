[[COMP26020]] - [[haskell]]

a typical error in haskell includes forgetting to define a function over some value:
```Haskell
oops True = True
print (oops False)
```
the function definition is valid, but this will return a runtime error - because `oops` doesn't know what to do in the case that it has been provided `False`

undefined recursion is also a common error
```Haskell
eep 0 = 0
eep n = 1 + eep n
```
how will `eep` ever reach the base case?