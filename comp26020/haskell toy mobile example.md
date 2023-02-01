[[COMP26020]] - [[haskell]]

```haskell
data ToyType Bird | Cloud | Meteor derives (Eq)

data Mobile = Toy ToyType | Stick Mobile Mobile

instance Eq Mobile where
	(Toy a) == (Toy b) = a == b
	(Stick w x) == (Stick y z) = ((w == y) && (x == z)) 
							|| ((w == z) && (x == y))
	_ == _ = False
```

- A mobile can either be a toy on its own, or a stick made up of two mobiles. This means we have made a recursive definition i.e. the toy on its own is the base case, and the step case is having a stick which holds two more mobiles

- We derive eq for the toytype in order to determine whether the objects in a mobile are equal to eachother

- We need the `_ == _ = False` line to handle cases where we may perform unexpected comparisons, for instance if we tried to compare a stick to a toy