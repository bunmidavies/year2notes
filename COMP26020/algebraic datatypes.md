[[COMP26020]] - [[haskell]]

> [!Algebraic Datatype]
> an algebraic datatype is a type where each possible element can have a specified shape. We define the different shapes through ==value constructors==

```haskell
data TypeName = value1 field1 field2 | value2 field1 field2
```

the 'algebra' in algebraic datatypes comes from the idea that:
- sum = `A | B` (A or B but not both)
- product = `A B` (A and B together to form a single structure) 

haskell already has one algebraic datatype builtin - the ==maybe== datatype
```haskell
Maybe a = Nothing | Just a
```

### binary tree algebraic datatype
```haskell
data Btree a = Tip | Node (Btree a) a (Btree a)
```

### list alegbraic datatype + head function
```Haskell
data MyList a = Empty | Append a (MyList a)
myHead :: MyList Int -> Maybe Int
myHead Empty = Nothing
myHead (Append x xs) = Just x
```

this is defining a basic recursive list structure, but haskell already has this implemented - [[haskell lists]]