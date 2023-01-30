[[COMP26020]] - [[haskell]]

following on from the previous part ([[error values in haskell + reasoning about errors]]), we've seen that haskell has the property where programs can terminate even if there are parts of data which if used, would cause the program not to terminate. But why may this be useful?

this becomes more useful when we combine this idea with recursive algebraic data types 

for example:
```haskell
ones = 1:ones
main = print(take 10 ones)
```
this will return "[1,1,1,1,1,1,1,1,1,1]" - so despite defining this data structure to be supposedly infinite, we're still able to get something from it when we apply a function to it

this means that if you need to take certain values from a potentially infinite data structure, you dont even need to define the finiteness of this data structure - haskell will generate the finite parts as needed. This allows for clean/conceptual code in haskell, where this may be a bit of a problem in an imperative language

we can define all natural numbers as follows:
```haskell
nats = 0:[n + 1 | n <- nats]
main = print(take 5 nats)
```
we see that 0,1,2,3,4 is printed when run

to retrieve an element by index, we use the ==!!== operator in haskell:
```haskell
main = print(nats !! 7)
```

we can use this operator to generate the fibonnacci numbers:
```haskell
fibb = 1:1:[(fibb !! n) + (fibb !! (n + 1))
			| n <- [0..]]
```

this means:
- when we start at 0, n = 0 so we're doing
  1:1:[fibb[0] + fibb[1]]
  1:1:[1 + 1] = 1:1:2

we can also define the prime numbers this way, but isnt as intuitive to figure out like fibonnacci is

```haskell
sieve :: [Int] -> [Int]
sieve [] = []
sieve (x:xs) = x:[y | y <- (sieve xs),
						y `mod` x /= 0]

primes = sieve [2..]
```

we can always use ==take== to then retrieve values from these infinite data structures