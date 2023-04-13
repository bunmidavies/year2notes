[[COMP26020]]

- lambda functions are a key part of functional programming languages, but a more recent feature in c++ ([[fp in C++]])

- anonymous functions / lambda functions were introduced in **c++ 11**
- lambda expressions are useful as:
	- they can be passed as arguments / returned from functions
	- they can be stored
	- they are first class citizens (act like normal variables)

- lambdas typically involve a capture which is contained within `[]` - this allows you to use names in the current scope outside of the lambda within the lambda's scope
- this is also known as **closure** in functional programming

- `[]` = capture nothing
- `[var]` = capture var by value
- `[&var]` = capture var by reference ([[references in C++]])
- `[=]` = capture **everything used in the lambda** by value where possible ?
- `[&]` = same as above, but capture by reference instead
- `[&,var]` = capture everything by reference, **apart from var**