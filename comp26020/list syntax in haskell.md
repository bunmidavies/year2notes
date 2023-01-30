[[COMP26020]] - [[haskell]]

it was previously shown how to create a list type from scratch, but haskell actually provides this ability to save time

to declare a list, any regular type can be wrapped in square brackets:
```haskell
myHead :: [a] -> Maybe a
myHead [] = Nothing
myHead (x:xs) = Just x

main = print(myHead ([1,2,3]))
```

strings can be represented as a list of chars, or just a string on its own:
```haskell
main = print(myHead (("Hi"::[Char])))
main = print(myHead (("Hi"::String)))
```

lists can also be defined shorthand:
```haskell
main = print([1..5])
-- 1,2,3,4,5
```

we can also create pairs through this same idea:
```haskell
l = [(w,n) | w <- "Hi!", n <- [1..3]]
```

additionally, conditions can be added in:
```haskell
l = [(w,n) | w <- "Hi!", n <- [1..3], w /= 'i']
```
this will return pairs without 'i' in