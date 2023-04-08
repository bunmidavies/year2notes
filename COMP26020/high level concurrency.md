[[COMP26020]]

### ~ definition
- as explained within previous sections, its possible to implement concurrent systems using things like locks, monitors, semaphores etc. ([[mutual exclusion + critical sections]] / [[monitors]]), and [[inter-process messaging]]
- however, to implement any of these methods as a programmer can be particularly tedious, and opens room for a lot of bugs / errors
- thus, there are alternative implementations which allow for concurrency, but abstract many details away from the programmer, in order to avoid bugs / errors in functionality

### ~ transactional memory
- transactional memory essentially provides an abstraction for managing concurrent access to memory, by managing memory accesses through ==transactions==, similar to databases
- the main downside is the overhead involved with transactional memory, but now if the atomicity of some data within transactional memory is violated, the process state can simply be rolled back

### ~ automatic concurrency
- automatic concurrency is essentially where ==the compiler implements concurrency==
- the programmer doesnt specify or manage any threads / processes or concurrency 'primitives', and instead relies on compiler / runtime optimisations to find opportunities for where concurrency is appropriate
- the main advantage of automatic concurrency is the potential increased performance of a program, with less chance of concurrency bugs introduced by the programmer, and less work from the programmer in general
- however, the capabilities of how a compiler can introduce concurrency is obviously limited, and in general is a very complex challenge 
- functional programming languages are better suited to automatic concurrency, since:
	- functions have no explicit ordering
	- functions have no state
	- data flow within fp languages is explicit
