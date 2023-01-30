[[COMP26020]] - [[haskell]]

we can define the accepted types for functions which take functions as inputs ([[higher order functions + alternate definitions]])

```Haskell
atTen :: (Int -> Bool) -> Bool
atTen f = f(10)
```

you could then also explicitly define the type of a lambda function provided

```Haskell
main = print(atTen((\x -> True)::Int -> Bool))
```
but typically, this notation isn't required

it is also possible to create our own types using the `data` keyword

```Haskell
data SwitchState = On | Off
isOn On = True
isOn Off = False

toggle On = Off
toggle Off = On

main = print(isOn(toggle On))
```
`False` will be printed, as On will be toggled to Off and isOn is defined to return False when given Off

custom pairs can also be defined by just writing multiple types on a line
```Haskell
data myPair = IntPair Int Int 
```

to convert to a custom type you can just write the type name followed by the data:

haskell can then infer when you are referring to a custom type you've made
```Haskell
data MyPair a b = Pair a b

myFirst (Pair a b) = a

main = print(myFirst(Pair 3 5))
```

a datatype which is constructed by giving multiple constructors depending on the data provided is known as an ==algebraic datatype== - the term 'algebraic' comes from the fact that the type constructor can be defined as a mathematical type term

haskell already has one algebraic datatype builtin - the ==maybe== datatype

as well as this, algebraic datatypes can be recursive
```Haskell
data MyList a = Empty | Append a (MyList a)
myHead :: MyList Int -> Maybe Int
myHead Empty = Nothing
myHead (Append x xs) = Just x
```

this is defining a basic recursive list structure, but haskell already has this implemented - [[haskell lists]]