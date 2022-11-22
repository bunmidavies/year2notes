[[COMP26020]]

C has two main ways of accessing data - normal variables and pointer variables. C++ adds a third way - references.
References in C++ are declared using an ampersand, `&` -  a reference variable will point to the memory address of an existing variable, such that any changes made to the reference variable's value will change the value of the original variable

What is the difference between references and pointers?
	- Both refer to another piece of data, but a reference has a normal syntax
	- A reference can never be null
	- A reference is always initialised (since it can never be null), and points to the same data for its lifetime

Why are references useful?
	- In C, passing by value means that you cannot modify the arguments passed into any function, given that you pass a certain variable into the function
	- A good example of this is where you write a function to swap two variables. Passing by value means that this will never work
	- Passing by pointer **will work** in C, but is awkward and its easy to get confused by the notation. Here's the working swap function with pointer passing:
```C
void swap(int* x, int* y)
{
	int tmp = *x;
	*x = *y;
	*y = tmp;
}
```

	- In C++, you can pass by reference and end up with simpler code:

```C++
void swap(int& x, int& y)
{
	int tmp = x;
	x = y;
	y = tmp;
}
```

	- References essentially eliminate the use of pointers in a number of situations: when we want to change the function paramaters, and pass large structures

C++ also supports **function overloading** - this allows for multiple functions to have the same name, but different types within their parameters (thus doing different things given the types of the parameters when called)