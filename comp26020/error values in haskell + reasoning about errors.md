[[COMP26020]] - [[haskell]]

```haskell
x = x
main = print(x)
```
the following code results in the program running forever, since x is not defined. This type of error is known as ==bottom==, because values you assign are ordered by how informative they are (from top to bottom), and doing the above assigns the least informative of all data values

when dealing with errors in haskell, it is best to follow the idea that there are ==no issues with the data provided== - i.e. they dont error out or cause the program to run forever. But it can also be useful to see what problems

to call an error in haskell, use the ==error== keyword

we are able to provide errors as values into functions, but note that if the argument is never used in the function, it doesn't matter if we provide an error. The error it won't be returned:
```haskell
eInt ::  Int
eInt = error "Hang on..."
g x = 5
main = print(g eInt)
```
5 will be printed here with no errors returned

if we do something like:
```haskell
eInt :: Int
eInt = error "Hang on..."

f x = x + 3
main = print(f eInt)
```
this will return the error, as we are actually trying to use the error in the function

this is the notion of ==strictness== - with the example above, f is ==strict== because if x is an error in its argument, then f can't return a well defined value. Meanwhile g is ==nonstrict== 

for instance, in haskell, the multiplication operation is ==strict== in both of its arguments when multiplied for 0:
```haskell
eInt * 0
```
and
```haskell
0 * eInt
```
will both return an error for this reason


in haskell, any functions can be used as infix functions using the backtick symbols
```haskell
stimes :: Int -> Int -> Int
stimes 0 n = 0
stimes m n = m * n

eInt = error "Hang on..."

main = print(0 `stimes` eInt)
```
the above code returns 0, while swapping the order of these returns the error - this is because stimes is programmed to look at its first argument

you might think this can be fixed by adding a case to handle the other way around, but this ==doesnt work==, due to the fact that both cases must ==always== be evaluated

==sequentiality== in haskell is the idea that any calculation be written in a single thread

#### errorPair question
is a pair defined as an error different to a pair of errors?

using the following code the question is answered:
```haskell
strangePair = (eInt,eBool)
ePair = error "Hang on..."

h :: (Int,Bool) -> Int
h (x,y) = 42

j :: (Int, Bool) -> Int
j p = 10

main = print(h strangePair)
```
this code demonstrates the following:
- calling j with a pair of errors or error both return 10
- calling h with an error pair will return 42
- calling h with a pair of errors will return an error

this demonstrates that in haskell there is a difference between operating with a pair and operating with a pair knowing what is actually ==inside the pair==

we can say that j is ==not strict== in its argument, but is h strict/non strict?

h can be called strict in its ==spine==, i.e. strict over the shape of the structure of the data