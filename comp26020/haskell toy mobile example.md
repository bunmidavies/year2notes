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