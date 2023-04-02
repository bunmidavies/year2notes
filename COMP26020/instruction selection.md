[[COMP26020]]

### definition
- instruction selection the 1st stage of the [[code generation]] process on the back-end of a compiler - it essentially involves matching IR patterns ([[middle-end of a compiler]]) to target code instructions
- locally optimal instructions can be selected, but global optimality is an ==NP-complete== problem
- within this stage, we assume that there are enough registers to perform everything that needs to be done - this can be sorted out later in [[register allocation]]

### example - arithmetic expressions
- some example operation `x+y` could generate the following target code (RISC-like assembly):
```pug
load r1, @x
load r2, @y
add r3, r1, r2
```
- the first issue is whether the registers in this example are already in use or not
- the compiler can also take advantage of commutativity / associativity, in order to slightly improve the code
- shifting is often faster than multiplication on many processors, so the compiler may aim to incorporate shift operations with addition over multiplication

### storing multidimensional arrays
- the compiler must decide on a memory storage scheme for arrays of 2 dimensions or more (in the following examples, we assume $n$ is the number of rows, and $m$ the number of columns) - the two main methods are:
	- ==row-major== - where values are laid out as a sequence of consecutive rows in memory. Given an element $[i][j]$, it is accessed at the address base+(i$*$(m+1)+j)$*$sizeof(element)
	- ==column-major== - where values are laid out as a sequence of consecutive columns in memory. Given an element $[i][j]$, it is accessed at the address base+(j$*$(n+1)+j)$*$sizeof(element)

### implementing functions / procedures
- in high level programming languages, functions are essential, meanwhile in low level hardware / languages, they're technically not supported
- therefore the compiler must generate code which ==emulates== the behaviour of a function / procedure
- ==method inlining== is a common technique, which involves just replacing the function call in source code with the actual body of that function - this is in the attempt to reduce the overhead related to moving parameters and return values from a function
![| 550](https://i.imgur.com/B6zgJEn.png)
