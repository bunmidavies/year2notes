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

***

[[algebraic datatypes]]