[[COMP26020]]

### intro
- at this point of compilation, we've received the partially optimised intermediate representation from the [[middle-end of a compiler]] - thus we are in the ==back-end== of the compiler, which is much more concerned with ==engineering== in comparison to the front-end
- in the back-end of the compiler, we generate the ==target code== - this is done with 2 main priorities:
	1. selecting correct target language instructions (a pattern matching problem)
	2. optimising the target code for the target platform
- the back-end can be split into 3 main steps:
	1. [[instruction selection]]
	2. [[register allocation]]
	3. [[instruction scheduling]]