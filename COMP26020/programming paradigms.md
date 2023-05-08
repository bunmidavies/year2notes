[[COMP26020]]

### definition
- a programming paradigm essentially defines a ==fundamental style of programming==
- programming languages can be classified using paradigms, and a single programming language may implement one or more paradigms
- the three main 'sub-paradigms' are:
	- object oriented: C++, C#, Java
	- functional: haskell
	- logical: prolog
- the two main paradigms which these subparadigms come under are:
	- imperative
	- declarative
- some paradigms are much better suited to specific kinds of software engineering problem, while others are not

### imperative programming languages
- imperative programming languages involves the programmer describing a ==sequence of statements== manipulating the program state
- imperative on its own (i.e. assembly) can get confusing as there are no control flow statements, so it can become difficult to follow the program
- the ==imperative structured== paradigm introduces advanced ==control flow operations==, e.g. loops, conditionals, functions - languages like C follow this structure, and are easier to follow than assembly
- the ==imperative object-oriented== paradigm introduces ideas like ==encapsulation==, and is suited to problems which may involve a lot of states - examples include C#, C++ etc
- the ==imperative concurrent== paradigm uses execution threads/processes to describe both interleaving and parallel computation flows - a lot of programming languages provide this functionality

### declarative programming paradigm
- the declarative programming paradigm involves the programmer describing the meaning/result of computations
- in these languages, there is a lot of abstraction, which can cause code to become very convoluted
- declarative programming languages can have the notion of ==pure functions== - functions with no side effects
- loops are also implemented with ==recursion==

![](https://i.imgur.com/XY75Jpe.png)
