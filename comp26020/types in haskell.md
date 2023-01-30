[[COMP26020]] - [[haskell]]

in haskell, ==types are checked at compile time==, and ==every expression has a type==

to explicitly define a functions type, use :: notation:
```Haskell
f :: Int -> Int
f x = x + 3
```

to explicitly define a parameter, :: notation is used again:
```
print(10::Double)
```
note that with f above, an error would now be returned as it isnt expecting a double

if a type isn't provided, haskell will try to ==infer== what the type should be - furthermore, haskell has a ==generic system==, which means if no type has been defined for a function, the function can work with multiple types
```Haskell
j x = False
main = print(j True && j 10)
```

we can also define generic types ourselves with a lowercase name:
```Haskell
j :: a -> Bool
```
`a` is known as a type variable, so j can essentially work for all input types