[[COMP26020]] - [[haskell]]

a typeclass in haskell is a group of operations, each of which can be applied when faced with a particular data type - it is comparable to an ==interface== in imperative languages. It is ==not like a class==

typeclasses are simply defined with the ==class== keyword:
```haskell
class Descriptive a where
	describe :: a -> String

instance descriptive Bool where
	describe True = "Yep!"
	describe False = "Don't bet on it!"

instance descriptive Int where
	describe 1 = "The loneliest number :("
	describe _ = "Another boring number."

main = print(describe (1::Int))
```
integers themselves in haskell are already overloaded, so for that reason the `::Int` needs to be added onto the end

to then create further functions which only apply on data types within a typeclass, we can use the `=>` notation
```haskell
descrLen :: Descriptive a => a -> Int
descrLen x = length(describe x)
```

we can use this when dealing with list structures:
```haskell
instance (Descriptive a) => Descriptive [a] where
	describe [] = "nothing else!"
	describe (x:xs) = (describe x) ++ ", then " ++ describe(xs)
```

if we want a data type to be part of multiple typeclasses, we can just comma separate these in brackets

in haskell, ==equality== itself has to be defined as a typeclass, because there are different types which can be comparable in the language. This is a built-in typeclass within the language

when you use symbols as a function name, it will automatically be interpreted as an ==infix operator== - to use it as normal, you must wrap the function in brackets

we can define a very basic equality typeclass as follows:
```haskell
class MyEq a where
	(===) :: a -> a -> Bool
	(=/=) :: a -> a -> Bool
	x =/= y = not(x === y)
```

[[haskell built in typeclasses]]