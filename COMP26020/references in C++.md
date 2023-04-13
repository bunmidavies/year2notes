[[COMP26020]] - [[C++]]

### references
- C has two main ways of accessing data - ==normal variables== and ==pointer variables==
- C++ adds a third way - ==references==
- references in C++ are declared using an ampersand, `&` 
- a reference variable points to the memory address of an existing variable, such that any changes made to the reference variable's value will change the value of the original variable

### references vs pointers
- both refer to another piece of data, but a reference has a normal syntax, and are dereferenced implicitly
- ==a reference can never be null, whereas pointers can be null==
- for the reason above, a reference is always initialised (since it can never be null), and points to the same data for its lifetime

### why are references useful? `swap()` example
- In C, passing by value means that you cannot modify the arguments passed into any function, given that you pass a certain variable into the function
- A good example of this is where you write a function to swap two variables. Passing by value means that this will never work, so you would have to use pointers in C
- Passing by pointer **will work** in C, but is awkward and its easy to get confused by the notation. Here's the working swap function with pointer passing:
```C
void swap(int* x, int* y)
{
	int tmp = *x;
	*x = *y;
	*y = tmp;
}
```

- In C++, by using references you can do the same thing with simpler code:
```C++
void swap(int& x, int& y)
{
	int tmp = x;
	x = y;
	y = tmp;
}
```

- ==references eliminate the use of pointers in different situations==:
	- when we want to alter the values of parameters being passed into a function
	- when we want to pass large structures into a function

