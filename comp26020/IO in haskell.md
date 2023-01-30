[[COMP26020]] - [[haskell]]

the idea in haskell is that input and output behaviour is modelled just by assigning values (like everything else in haskell)

essentially, a haskell program is an element of an IO type - it only ever looks at the definition of `main`. The compiler just looks for this definition, and carries out the behaviour specified

IO can also be captured with the `IO String` data type:
```haskell
main = (getLine:: IO String)
```

