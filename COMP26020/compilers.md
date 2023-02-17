[[COMP26020]]

- A compiler is a program that acceps as inputs a program text in a certain language and produces as output a program text in another language, while preserving the meaning of that text

- a compiler will produce code that runs faster than an interpreter

- a compiler must preserve the meaning of the program being compiled and 'improve' the source code in some way. A number of factors compilers may be concerned with include;
	- speed
	- space
	- feedback
	- debugging
	- compilation time efficiency

- for different purposes, these may be different levels of priority for the compiler

- there are two major phases when converting source code to target code - ==analysis== and ==synthesis==
	- analysis is also known as the ==front-end== stage, where legal/illegal parts of the program are recognised, and an intermediate representation is created
	- the ==back-end== part of compilation is synthesis - the compiler chooses which instructions are used to implement each intermediate representation operation

==Generally, analysis is O(n) while synthesis is NP-complete==
automation has been much less successful with synthesis than it has been with analysis