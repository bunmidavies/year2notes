[[COMP26020]]

modern c++ is able to treat functions like data, but is unable to **reason about them**, which is a key part of any functional language

- the [[c++ standard library]] has a number of methods which are functional-like:
	- transform() applies a function on a range and stores it in another range ([[c++ iterators]])
	- copy_if() copies elements in a range to another range if they meet some rule
	- reduce() reduces a range into a single value by applying a function to every element
- in the sense that, **they are functions that take functions as inputs**

the FP equivalents for above are:
- transform = map
- copy_if = filter
- reduce = fold

- [[lambda functions in c++]] didn't always exist, but are useful for a number of reasons