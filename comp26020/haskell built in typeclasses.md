[[COMP26020]] - [[haskell]]

haskells built in typeclasses include the following:
- `Show` - instances have to implement a function called show (a -> String). used for print() in haskell

by using the ==deriving== keyword, we can grab default implementations of certain operators, in order to allow user defined types to be used with built in functions