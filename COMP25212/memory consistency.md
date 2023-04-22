[[COMP25212]]

### ~ definition
- memory consistency involving multiple cores is essentially the idea that:
	- a read operation returns the same value from all cores
	- a write operation updates all cores before any other operation takes place
- this can be difficult to implement since sometimes a thread may need to read and update a variable as a single ==atomic== operation, thus no other thread can read/write that variable when this operation is taking place

### ~ simple consistency problem example
![ | 450](https://i.imgur.com/jsLLjaM.png)

### ~ sequential consistency
- sequential consistency is basically a term that exists to describe an ideal consistency existing in a multicore system, which most software developers expect
- *"the result of any execution is the same as if the operations of all teh processors were executed in some sequential order, and the operations of each individual processor appear in this sequence in the order specified by its programs"*
	1. memory operations ==appear== to execute one after another
	2. all threads see write operations in the same order
	3. operations within a thread ==appear== to execute in the order the program describes
- the compiler must insert special instructions in order to maintain program semantics with consistency:
	1. ==fence== - all memory accesses before the fence must complete before starting to execute other ones
	2. ==barrier== - all threads need to reach the barrier before any can continue to execute
	3. ==lock== - only one thread can proceed to an atomic section
![](https://i.imgur.com/VS6dd9s.png)


### ~ ISA support for synchronisation

- ==Load-Linked / LL x== - hardware locks the cache line corresponding to x and returns its contents
- ==Store-Conditional / SC x, y== - hardware checks if any instruction has modified x since LL, if not then store y - otherwise x is unmodified
- ==transactional memory== - execute atomic sections assuming no conflicts, and roll back memory changes if there was any conflict (and commit if not)
![ | ](https://i.imgur.com/edq2YgW.png)