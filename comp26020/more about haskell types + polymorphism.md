[[COMP26020]] - [[haskell]]

we've seen that haskell can support polymorphism:
```haskell
f :: a -> Bool
f _ = True

main = print((f 7) && (f True))
```
we have one definition of f here which can be applied to different types, and we have done this using a ==type variable==

there are two main types of polymorphism:
- ==parametric== polymorphism: where the function applied has to be the ==same== for all possible types
- ==ad-hoc== polymorphism

an issue with parametric polymorphism is as follows:
```haskell
g :: (b -> Bool) -> Bool
g h = (h 7) && (h True)

main = print(g f)
```
we receive an error to do with 'rigid type variable' if we try to run this. The problem is as follows - in our type definition for g, we've defined the function as `(b -> Bool)`, which implicitly implies all types of `b` should work with `h 7` and `h True`

a better example is as follows
```haskell
p :: (a,a)
p = (True, True)
```
the problem with this is that haskell interprets this as
```haskell
p = forall a. (a, a)
```
meaning its expecting `(True, True)` to be a pair of Strings, Integers, all at once

==ad-hoc polymorphism== is also known as ==overloading==, and is where the same function name can mean different things based on the data type
for instance, you can add ints and you can add doubles in haskell