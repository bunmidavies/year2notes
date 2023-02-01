[[COMP26020]] - [[haskell]]

haskells built in typeclasses include the following:
- `Show` - instances have to implement a function called show (a -> String). used for print() in haskell
- `Eq` - instances have to implement the `==` function. Note that because `\=` is just the opposite of `==`, it can actually just be defined as the opposite of `==` without having to be defined in the classes which are instances of the `Eq` typeclass

by using the ==deriving== keyword, we can grab default implementations of certain operators, in order to allow user defined types to be used with built in functions