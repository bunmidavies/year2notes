[[COMP26020]] - [[haskell]]

a typeclass is a group of operations/functions, each of which can be applied to a given type

a type is ==part of a typeclass== if it supports and implements all the operations that typeclass describes. We describe a type that implements a typeclass as an ==instance of the typeclass==

for example, in Haskell itself `Eq` and `Show` are typeclasses which the regular built-in types like `Int`,`Bool`, etc. are all ==instances== of

```haskell
class Descriptive a where
	describe :: a -> String

instance Descriptive Bool where
	describe True = "Yep!"
	describe False = "Don't bet on it!"

instance Descriptive Int where
	describe 1 = "The loneliest number :("
	describe _ = "Another boring number."

main = print(describe (1::Int))
```

- we define the typeclass with the `class` keyword
- we make a type an ==instance of the typeclass== by using `instance`, and then providing implementations for the functions described within the typeclass
- once this is done, we can then use any of the typeclass's functions on types which are instances of the typeclass

Lecture: *integers themselves in haskell are already overloaded, so for that reason the `::Int` needs to be added onto the end*

we can then create functions which are only applicable to types which are instances of a given typeclass

```haskell
descrLen :: Descriptive a => a -> Int
descrLen x = length(describe x)
```
since types which aren't instances of the `descriptive` class won't have the `describe` functionality, we use the `=>` notation to say `a` ==must be an instance of Descriptive==



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