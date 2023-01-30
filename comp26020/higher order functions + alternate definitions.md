[[COMP26020]] - [[haskell]]

as mentioned earlier, in haskell functions should behave like any other data
therefore it should be possible to write a ==function that outputs another function==

```Haskell
addConst n m = n + m
addThree = addConst 3
```

printing `addThree 7` will return 10. There is a more explicit way of defining these functions:

```Haskell
addConst n = \m -> n + m
```

it should also be possible to write a function which takes ==functions as inputs==
```Haskell
thriceFromZero f = f(f(f(0)))
```

printing `thriceFromZero(addConst 3)` will return 9 - this is due to the original `addConst` being called against 0, then addConst being called to 3 creating 6, then addConst being called to 6 creating 9

haskell also allows the ability to write anonymous functions - i.e. functions on the fly
```
thriceFromZero((\n -> 2*n + 1))
```

haskell always takes the most ==recent== definition of a value to be used, e.g.
```Haskell
h n = (\n -> n)
```
calling `h 1 2` will return 2
this is known as ==shadowing==

recursive higher order functions can be defined using the base case, then general:
```Haskell
repFromZero 0 f = 0
repFromZero n f = f(repFromZero (n-1) f)
```

functions can be defined by case as well:
```Haskell
small n = case n of
 0 -> True
 1 -> True
 n -> False
```
this also allows us to modify `n` easily

we also have the ability to define what is similar to ==local variables==:
```Haskell
sideOfFive n
 | d -> -1
 | d -> 0
 | d -> 1
 where d = n - 5
```
the guard expressions (`|`) are required in order to use the `where` expression

another type of 'local variable' can be declared by using ==let==
```Haskell
z = let x = 10 in
 let x = 20 in x
```

`let` doesn't work sequentially - for instance:
```Haskell
w = let x = 5 in
 let f = \n -> x in
 let x = 6 in
 f 0
```

what this code basically does is define a bunch of 'local variables' before actually assigning anything to `w` - the only thing which is assigned to `w` is whatever is returned from `f 0`

because x was equal to 5 when f was declared, x equalling 6 when f is called doesn't affect f. 5 will still be returned