[[COMP26020]] - [[haskell]]

the idea in haskell is that input and output behaviour is modelled just by assigning values (like everything else in haskell)

essentially, a haskell program is an element of an IO type - it only ever looks at the definition of `main`. The compiler just looks for this definition, and carries out the behaviour specified

IO can also be captured with the `IO String` data type:
```haskell
main = (getLine:: IO String)
```

but with this code alone, nothing can happen. There is no way of turning an input into a mathematical value which can be used in the functions you create in haskell, since its impossible to tell what will be inputted

to use input, then we use the `>>=` operator, which takes an IO object, a function which maps mathematical values to IO, and returns an IO object
```haskell
>>= :: IO b -> (b -> IO c) -> IO c
```
==print== is already an example of an operator of the `b -> IO c` type

the IO empty tuple is represented as ==IO ()==, and is used to represent when there is nothing sensible to return, so just nothing is returned instead:
```haskell
greet :: String -> IO ()
greet n = print ("Hi " ++ n)
main = getLine >>= (\n -> greet n)
```

IO can also be recursively defined like everything else in haskell
```haskell
main = putStrLn "Who is the greatest?" >>
		getLine >>=
		\n -> if n == "Joe"
				then putStrLn "Don't forget it!"
				else (putStrLn "Be serious!" >> 
						main)
```


we may find that in some cases we have to keep writing bind operators, and this can become tedious. ==Do notation== allows you to easily assign the output of a getLine into a data type:
```haskell
main = do
	putStrLn "Enter a name:"
	n <- getLine
	putStrLn "Enter another name:"
	m <- getLine
	putStrLn ("Hi " ++ n ++ " and " ++ m)
```